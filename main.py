from alsong import ALSong
import time
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <artist> <title>")
        sys.exit(1)

    artist = sys.argv[1]
    title = sys.argv[2]

    
    print(f"Searching for lyrics for {artist} - {title}")
    begin = time.time()
    user_lyrics = ALSong.search_lyrics(artist=artist, title=title)
    if not user_lyrics:
        print("No lyrics found")
        sys.exit(1)
    end = time.time()
    print(f"Found {len(user_lyrics)} user lyrics in %.2fs" % (end - begin))

    user_lyrics = user_lyrics[0]

    print(f"Getting first live lyrics for {artist} - {title}")
    begin = time.time()
    live_lyrics = ALSong.get_live_lyrics(user_lyrics)
    end = time.time()
    print(f"Got live lyrics in %.2fs" % (end - begin))
    
    print()
    print("-----------")
    print()
    for lyric in live_lyrics.lines:
        print(f"{lyric.time}s\t\t {lyric.text}")
    