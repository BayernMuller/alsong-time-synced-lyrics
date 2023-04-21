from attr import dataclass
from typing import List

@dataclass
class Lyric:
    lyricID: int
    artist: str
    title: str
    album: str

@dataclass
class Line:
    time: float
    text: str

@dataclass
class LiveLyrics:
    lines: List[Line] = list()
    authour: str = ""