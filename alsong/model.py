from typing import List, Optional
from pydantic import BaseModel

class Lyric(BaseModel):
    lyricID: int
    artist: str
    title: str
    album: str
class Line(BaseModel):
    time: float
    text: str

class Author(BaseModel):
    name: Optional[str] = None
    mail: Optional[str] = None
    homepage: Optional[str] = None
    comment: Optional[str] = None
class LiveLyrics(BaseModel):
    lines: Optional[List[Line]] = []
    author: Optional[str] = None
    info: Optional[str] = None
