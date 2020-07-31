# ForReddit-Meme-to-Chromecast
    
# Summary 
  Grab memes from a subreddit for memes, I will use r/highqualitymemes, and send them to a google photos folder for
  a chromecast to use as wallpapers for a TV. USES: Reddit API, Google Photos API, python3+. This is a very basic
  python3 script intended for individual home use. 

# Pre-Req
  - install python3
  - install pip
  - install Pillow:
    - `pip install Pillow`
  - install praw:
    - `pip install praw`
  - install pandas:
    - `pip install pandas`

# Run
    python3 forreddit_to_cast.py -s memes -l 20
    or
    python3 forreddit_to_cast.py
  - arguments: 
    - --sub or -s: for choosing your sub. ex memes or highqualitymemes
    - --limit or -l: for choosing the limit of images that are downloaded ex 10,20,30,50,100
