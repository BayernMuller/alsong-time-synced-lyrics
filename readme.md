<p align="center">
    <img src="res/logo.webp"></img>
</p>


<span align="center">

# alsong-time-synced-lyrics

</span>


### What is this?
* This is [Alsong](https://www.altools.co.kr/download/alsong.aspx) lyrics database client for Python.
* You can get time-synced lyrics from Alsong server.
* I catched the request from Alsong client with Wireshark and implemented the request in Python.

### Installation
* with pip
```bash
pip install git+https://github.com/BayernMuller/alsong-time-synced-lyrics
```

* with git
```bash
git clone https://github.com/BayernMuller/alsong-time-synced-lyrics
cd alsong-time-synced-lyrics
python setup.py install
```

### Usage
```bash
$ alsong "Led Zeppelin" "Black Dog" | jq
```
<details><summary><b>Click to view full result of Black Dog<b></summary>

```json
{
  "lines": [
    {
      "time": 7.12,
      "text": "Hey, hey, mama, said the way you move,"
    },
    {
      "time": 9.09,
      "text": "gonna make you sweat, gonna make you groove."
    },
    {
      "time": 18.7,
      "text": "Oh, oh, child, way you shake that thing,"
    },
    {
      "time": 20.97,
      "text": "gonna make you burn, gonna make you sting."
    },
    {
      "time": 29.99,
      "text": "Hey, hey, baby, when you walk that way,"
    },
    {
      "time": 32.35,
      "text": "watch your honey drip, can't keep away."
    },
    {
      "time": 53.69,
      "text": "*Ah yeah, ah yeah, ah, ah, ah."
    },
    {
      "time": 59.24,
      "text": "Ah yeah, ah yeah, ah, ah, ah."
    },
    {
      "time": 64.68,
      "text": "I gotta roll, can't stand still,"
    },
    {
      "time": 68,
      "text": "got a flame in my heart,"
    },
    {
      "time": 69.5,
      "text": "can't get my fill."
    },
    {
      "time": 75.93,
      "text": "Eyes that shine burning red,"
    },
    {
      "time": 78.99,
      "text": "dreams of you all through my head."
    },
    {
      "time": 89.09,
      "text": "Ah ah ah ah ah ah ah ah ah ah ah ah ah."
    },
    {
      "time": 100.27,
      "text": "Hey, baby, oh, baby, pretty baby,"
    },
    {
      "time": 104.38,
      "text": "Tell me won't you you do me now."
    },
    {
      "time": 124.2,
      "text": "Didn't take too long 'fore I found out,"
    },
    {
      "time": 127.16,
      "text": "what people mean my down and out."
    },
    {
      "time": 135.95,
      "text": "Spent my money, took my car,"
    },
    {
      "time": 138.41,
      "text": "started telling her friends"
    },
    {
      "time": 140.09,
      "text": "she wants to be a star."
    },
    {
      "time": 147.21,
      "text": "I don't know but I been told,"
    },
    {
      "time": 149.7,
      "text": "a big-legged woman ain't got no soul."
    },
    {
      "time": 153.87,
      "text": "* Chorus"
    },
    {
      "time": 182.23,
      "text": "All I ask for when I pray,"
    },
    {
      "time": 184.07,
      "text": "steady rollin' woman gonna come my way."
    },
    {
      "time": 192.98,
      "text": "Need a woman gonna hold my hand,"
    },
    {
      "time": 195.78,
      "text": "won't tell me no lies, make me a happy man."
    }
  ],
  "author": {
    "name": "oksk",
    "mail": "hi_bonobono@msn.com",
    "homepage": null,
    "comment": null
  },
  "info": {
    "lyricID": 547908,
    "artist": "led zepplin",
    "title": "black dog",
    "album": "Led Zepplin - Black Dog"
  }
}
```

</details>

```bash
$ alsong "Metallica" "The Unforgiven" | jq
```
<details><summary><b>Click to view full result of The Unforgiven<b></summary>

```json
{
  "lines": [
    {
      "time": 2.23,
      "text": "The Unforgiven"
    },
    {
      "time": 3.45,
      "text": "[HETFIELD/ULRICH/HAMMET]"
    },
    {
      "time": 56.29,
      "text": "New blood joins this earth"
    },
    {
      "time": 59.68,
      "text": "And quikly he's subdued"
    },
    {
      "time": 62.53,
      "text": "Through constant pained disgrace"
    },
    {
      "time": 66,
      "text": "The young boy learns their rules"
    },
    {
      "time": 69.56,
      "text": "With time the child draws in"
    },
    {
      "time": 72.85,
      "text": "This whipping boy done wrong"
    },
    {
      "time": 76.47,
      "text": "Deprived of all his thoughts"
    },
    {
      "time": 79.96,
      "text": "The young man struggles on and on he's known"
    },
    {
      "time": 85.11,
      "text": "A vow unto his own"
    },
    {
      "time": 88.4,
      "text": "That never from this day"
    },
    {
      "time": 91.62,
      "text": "His will they'll take away"
    },
    {
      "time": 98.41,
      "text": "What I've felt"
    },
    {
      "time": 99.89,
      "text": "What I've known"
    },
    {
      "time": 101.48,
      "text": "Never shined through in what I've shown"
    },
    {
      "time": 104.96,
      "text": "Never be"
    },
    {
      "time": 106.54,
      "text": "Never see"
    },
    {
      "time": 108.81,
      "text": "Won't see what might have been"
    },
    {
      "time": 111.85,
      "text": "What I've felt"
    },
    {
      "time": 113.4,
      "text": "What I've known"
    },
    {
      "time": 115.8,
      "text": "Never shined through in what I've shown"
    },
    {
      "time": 118.69,
      "text": "Never free"
    },
    {
      "time": 120.28,
      "text": "Never me"
    },
    {
      "time": 122.61,
      "text": "So I dub thee unforgiven"
    },
    {
      "time": 131.63,
      "text": "They dedicate their lives"
    },
    {
      "time": 134.81,
      "text": "To running all of his"
    },
    {
      "time": 138.27,
      "text": "He tries to please them all"
    },
    {
      "time": 141.64,
      "text": "This bitter man he is"
    },
    {
      "time": 145.09,
      "text": "Throughout his life the same"
    },
    {
      "time": 148.29,
      "text": "He's battled constantly"
    },
    {
      "time": 151.9,
      "text": "This fight he cannot win"
    },
    {
      "time": 155.4,
      "text": "A tired man they see no longer cares"
    },
    {
      "time": 160.72,
      "text": "The old man then prepares"
    },
    {
      "time": 164.09,
      "text": "To die regretfully"
    },
    {
      "time": 167.51,
      "text": "That old man here is me"
    },
    {
      "time": 173.87,
      "text": "What I've felt"
    },
    {
      "time": 175.26,
      "text": "What I've known"
    },
    {
      "time": 177.17,
      "text": "Never shined through in what I've shown"
    },
    {
      "time": 180.45,
      "text": "Never be"
    },
    {
      "time": 182.08,
      "text": "Never see"
    },
    {
      "time": 184.44,
      "text": "Won't see what might have been"
    },
    {
      "time": 187.51,
      "text": "What I've felt"
    },
    {
      "time": 189.11,
      "text": "What I've known"
    },
    {
      "time": 191.23,
      "text": "Never shined through in what I've shown"
    },
    {
      "time": 194.1,
      "text": "Never free"
    },
    {
      "time": 195.73,
      "text": "Never me"
    },
    {
      "time": 198.05,
      "text": "So I dub the unforgiven"
    },
    {
      "time": 273.44,
      "text": "What I've felt"
    },
    {
      "time": 274.93,
      "text": "What I've known"
    },
    {
      "time": 276.87,
      "text": "Never shined through in what I've shown"
    },
    {
      "time": 280.12,
      "text": "Never be"
    },
    {
      "time": 281.73,
      "text": "Never see"
    },
    {
      "time": 284.14,
      "text": "Won't see what might have been"
    },
    {
      "time": 287.29,
      "text": "What I've felt"
    },
    {
      "time": 288.78,
      "text": "What I've known"
    },
    {
      "time": 290.97,
      "text": "Never shined through in what I've shown"
    },
    {
      "time": 293.87,
      "text": "Never free"
    },
    {
      "time": 295.43,
      "text": "Never me"
    },
    {
      "time": 297.82,
      "text": "So I dub the unforgiven"
    },
    {
      "time": 314.98,
      "text": "Never free"
    },
    {
      "time": 316.14,
      "text": "Never me"
    },
    {
      "time": 318.52,
      "text": "So I dub the unforgiven"
    },
    {
      "time": 328.53,
      "text": "You labeled me"
    },
    {
      "time": 330.05,
      "text": "I'll label you"
    },
    {
      "time": 332.28,
      "text": "So I dub the unforgiven"
    },
    {
      "time": 342.45,
      "text": "Never free"
    },
    {
      "time": 343.88,
      "text": "Never me"
    },
    {
      "time": 346.28,
      "text": "So I dub the unforgiven"
    },
    {
      "time": 355.84,
      "text": "You labeled me"
    },
    {
      "time": 357.79,
      "text": "I'll label you"
    },
    {
      "time": 359.94,
      "text": "So I dub the unforgiven"
    },
    {
      "time": 367.82,
      "text": "Nit Rock ManiaClub ... Angel's Wings"
    },
    {
      "time": 368.76,
      "text": "cyworld.com/vusrmsdyd"
    }
  ],
  "author": {
    "name": "YoUN",
    "mail": "time_youn@hanmail.net",
    "homepage": null,
    "comment": null
  },
  "info": {
    "lyricID": 979860,
    "artist": "Metalica",
    "title": "The Unforgiven",
    "album": "Metallica - The Unforgiven"
  }
}
```

</details>
