import requests
from typing import List, Dict
import xml.etree.ElementTree as ET
from alsong.model import *
import re

class ALSong:
    __HEADERS = {'Content-Type': 'application/soap+xml; charset=utf-8', 'User-Agent': 'gSOAP/2.7', 'SOAPAction': 'ALSongWebServer/GetResembleLyricList2'}
    __URL = 'http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx'

    @staticmethod
    def search_lyrics(artist, title, page=1):
        response = ALSong.__alsong_request('GetResembleLyricList2', {'title': title, 'artist': artist, 'pageNo': str(page)})
        return ALSong.__parse_list(response.text)

    @staticmethod
    def get_live_lyrics(lyric: Lyric):
        response = ALSong.__alsong_request('GetLyricByID2', {'lyricID': str(lyric.lyricID)})
        live_lyric = ALSong.__parse_live_lyrics(response.text)
        live_lyric.info = lyric
        return live_lyric
    
    @staticmethod
    def __alsong_request(topic: str, data: Dict[str, str]):
        encryped_data = ''.join([f'<ns1:{key}>{value}</ns1:{key}>' for key, value in data.items()])
        encryped_code = "<ns1:encData>a8e4e6dbcd813026f6d2d832852fb72295b3862e098b213c581e9d7d5364bc58ed85e0b95304597c77fa2dfaacab73b044ebe0f63d304f902357b407affab92ed6a4600b36b767cd2e9d70ad9502f79ecc2e9941c1cc92c832dc6f1826b627f32d37fd51400a6fd2f6b396c399ffa08ed90938d484fcf50ad351f9d3d8860c2c</ns1:encData>"
        content = f"""<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns2="ALSongWebServer/Service1Soap" xmlns:ns1="ALSongWebServer" xmlns:ns3="ALSongWebServer/Service1Soap12"><SOAP-ENV:Body><ns1:{topic}>{encryped_code}{encryped_data}</ns1:{topic}></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
        return requests.post(ALSong.__URL, data=content, headers=ALSong.__HEADERS)

    @staticmethod
    def __parse_list(xml_data: str):
        root = ET.fromstring(xml_data).find('.//{ALSongWebServer}GetResembleLyricList2Result')
        lyrics = []
        for lyric in root:
            lyric_data = {data.tag.replace('{ALSongWebServer}', ''): data.text for data in lyric}
            lyrics.append(Lyric(**lyric_data))
        return lyrics
    
    @staticmethod
    def __parse_xml_tag(root, tag):
        xml_tag = root.find(f'.//{{ALSongWebServer}}{tag}')
        return xml_tag.text if xml_tag is not None else None

    @staticmethod
    def __parse_live_lyrics(xml_data: str):
        root = ET.fromstring(xml_data)
        lyric = ALSong.__parse_xml_tag(root, 'lyric')
        author = Author(
            name=ALSong.__parse_xml_tag(root, 'registerName'),
            mail=ALSong.__parse_xml_tag(root, 'registerMail'),
            homepage=ALSong.__parse_xml_tag(root, 'registerHomeURL'),
            comment=ALSong.__parse_xml_tag(root, 'registerComment')
        )

        live_lyrics = LiveLyrics()
        time_regex = re.compile(r'\[(\d{2}):(\d{2})\.(\d{2})\]')
        lyrics = [i for i in lyric.split('\n') if i]
        for line in lyrics:
            time = time_regex.search(line)
            line = time_regex.sub('', line).strip()
            if time:
                time = int(time.group(1)) * 60 + int(time.group(2)) + int(time.group(3)) / 100
                if int(time):
                    live_lyrics.lines.append(Line(time=time, text=line))
        
        live_lyrics.author = author
        return live_lyrics