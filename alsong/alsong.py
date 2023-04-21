import requests
import xml.etree.ElementTree as ET
from typing import List
from alsong.model import Lyric, LiveLyrics, Line
import re

class ALSong:
    __HEADERS = {'Content-Type': 'application/soap+xml; charset=utf-8', 'User-Agent': 'gSOAP/2.7', 'SOAPAction': 'ALSongWebServer/GetResembleLyricList2'}

    @staticmethod
    def search_lyrics(artist, title) -> List[Lyric]:
        data = '<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns2="ALSongWebServer/Service1Soap" xmlns:ns1="ALSongWebServer" xmlns:ns3="ALSongWebServer/Service1Soap12"><SOAP-ENV:Body><ns1:GetResembleLyricList2><ns1:encData>a8e4e6dbcd813026f6d2d832852fb72295b3862e098b213c581e9d7d5364bc58ed85e0b95304597c77fa2dfaacab73b044ebe0f63d304f902357b407affab92ed6a4600b36b767cd2e9d70ad9502f79ecc2e9941c1cc92c832dc6f1826b627f32d37fd51400a6fd2f6b396c399ffa08ed90938d484fcf50ad351f9d3d8860c2c</ns1:encData><ns1:title>{title}</ns1:title><ns1:artist>{artist}</ns1:artist><ns1:pageNo>1</ns1:pageNo></ns1:GetResembleLyricList2></SOAP-ENV:Body></SOAP-ENV:Envelope>'
        data = data.format(artist=artist, title=title).encode('utf-8')
        response = requests.post('http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx', data=data, headers=ALSong.__HEADERS)
        return ALSong.__parse_list(response.text)

    @staticmethod
    def get_live_lyrics(lyric: Lyric):
        data = '<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns2="ALSongWebServer/Service1Soap" xmlns:ns1="ALSongWebServer" xmlns:ns3="ALSongWebServer/Service1Soap12"><SOAP-ENV:Body><ns1:GetLyricByID2><ns1:encData>a8e4e6dbcd813026f6d2d832852fb72295b3862e098b213c581e9d7d5364bc58ed85e0b95304597c77fa2dfaacab73b044ebe0f63d304f902357b407affab92ed6a4600b36b767cd2e9d70ad9502f79ecc2e9941c1cc92c832dc6f1826b627f32d37fd51400a6fd2f6b396c399ffa08ed90938d484fcf50ad351f9d3d8860c2c</ns1:encData><ns1:lyricID>{id}</ns1:lyricID></ns1:GetLyricByID2></SOAP-ENV:Body></SOAP-ENV:Envelope>'
        data = data.format(id=lyric.lyricID).encode('utf-8')
        response = requests.post('http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx', data=data, headers=ALSong.__HEADERS)
        return ALSong.__parse_live_lyrics(response.text)

    @staticmethod
    def __parse_list(xml_data: str):
        root = ET.fromstring(xml_data)[0][0][0]
        lyrics = []
        for lyric in root:
            lyric_data = {data.tag.replace('{ALSongWebServer}', ''): data.text for data in lyric}
            lyrics.append(Lyric(**lyric_data))
        return lyrics

    @staticmethod
    def __parse_live_lyrics(xml_data: str):
        regex = re.compile(r'<lyric>(.*?)</lyric>', re.DOTALL)
        lyrics = regex.search(xml_data).group(1).strip().split('\n')
        live_lyrics = LiveLyrics()

        time_regex = re.compile(r'\[(\d{2}):(\d{2})\.(\d{2})\]')
        for lyric in lyrics:
            time = time_regex.search(lyric)
            lyric = time_regex.sub('', lyric).strip()
            if time:
                time = int(time.group(1)) * 60 + int(time.group(2)) + int(time.group(3)) / 100

            if int(time):
                live_lyrics.lines.append(Line(time=time, text=lyric))
            
        return live_lyrics