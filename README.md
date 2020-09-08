# Meme-to-CC

# Table of Contents

- [Dev Progress](https://github.com/WalterMitty2112/Meme-to-CC#currently-under-development)
- [Summary](https://github.com/WalterMitty2112/Meme-to-CC#summary)
- [Pre-Reqs](https://github.com/WalterMitty2112/Meme-to-CC#pre-req)
- [Run](https://github.com/WalterMitty2112/Meme-to-CC#run)

## CURRENTLY UNDER DEVELOPMENT
#### Known working components:
   - python script meme_to_cc.py
      - can download memes from specific subreddit and fix them to fit the size of a standard 1080p or 4k tv
   - grab albums ID from google photos API
#### Not working components:
   - empty old album
   - upload photos 
   - self deploying shell script (windows and linux)
      - script to run the python script at a set time everyday to grab new memes

## Summary 
  Grab memes from a subreddit for memes, I will use r/highqualitymemes, and send them to a google photos folder for
  a chromecast to use as wallpapers for a TV. This is a very basic python3 script intended for individual home use.
  
  All backgrounds for each meme are found in resources/bgmemes, they can be replaced or added to as long as the new image size follows a 16:9 aspect ratio and is greater than 1920x1080 or 2048x1164 which is the exact size that chromecast favors. Ex. base.jpg and base2.jpg are formatted for chromecast already
  
  The Meme Formatter I wrote is used to take each meme and add it to a background after resizing it if needed. All backgrounds can be replaced but I chose these because some are from memes and some are just nice as wallpapers. The best results come from wallpapers that are singular colors, this distracts less from the meme.
  
  - USES: Reddit API, Google Photos API, python3+, Java 1.8, [Meme formatter](https://github.com/WalterMitty2112/Meme-Formatter-for-Chromecast)

## Pre-Req

NOTE: All of this will be added to dev package when finalized

  - change 'redditAPI.txt' values to match your own
    - get your Reddit API keys at [reddit](https://www.reddit.com/prefs/apps)
  - download your google photos API key json file and put it in the project directory
  - install python3
  - install pip
    - `python3 -m install pip`
  - install Pillow:
    - `pip install Pillow`
  - install praw:
    - `pip install praw`
  - install pandas:
    - `pip install pandas`

## Run
Run any of these variations in a cmd or terminal 
```
python3 forreddit_to_cast.py -s memes -l 20 -a vroom
python3 forreddit_to_cast.py -m all_memes -l 150 -a vroom
python3 forreddit_to_cast.py -s me_irl
python3 forreddit_to_cast.py -m all_memes
python3 forreddit_to_cast.py -l 50
python3 forreddit_to_cast.py
```
  - arguments: 
    - --sub or -s: for choosing your sub. ex memes or highqualitymemes
    - --multi or -m: for chooing a multireddit on your reddit acct ex all_memes @Red-CC
    - --limit or -l: for choosing the limit of images that are downloaded ex 10,50,100,...
    - --album or -a: for distinguishing the album name to add photos too
    - NOTE: Arguments can be run separately, default values will be used for either except for album
    - default values are:
        - sub: memes
        - limit: 5
        - no default value for multireddit or album
