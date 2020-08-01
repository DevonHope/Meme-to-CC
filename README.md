# Meme-to-CC

# Table of Contents

- [Dev Progress](https://github.com/WalterMitty2112/Meme-to-CC#currently-under-development)
- [Summary](https://github.com/WalterMitty2112/Meme-to-CC#summary)
- [Pre-Reqs](https://github.com/WalterMitty2112/Meme-to-CC#pre-req)
- [Run](https://github.com/WalterMitty2112/Meme-to-CC#run)

## CURRENTLY UNDER DEVELOPMENT
#### Known working components:
   - python script forreddit_to_cast.py
      - can download memes from specific subreddit and fix them to fit the size of a standard 1080p or 4k tv
#### Not working components:
   - uploadTool
   - self deploying shell script (windows and linux)
      - script to run the python script and java script at a set time everyday to grab new memes

## Summary 
  Grab memes from a subreddit for memes, I will use r/highqualitymemes, and send them to a google photos folder for
  a chromecast to use as wallpapers for a TV. This is a very basic python3 script intended for individual home use. 
  - USES: Reddit API, Google Photos API, python3+, Java 1.8, [Meme formatter](https://github.com/WalterMitty2112/Meme-Formatter-for-Chromecast)

## Pre-Req
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
  - install java 1.8

## Run
Run any of these variations in a cmd or terminal 
```
python3 forreddit_to_cast.py -s memes -l 20
python3 forreddit_to_cast.py -s me_irl
python3 forreddit_to_cast.py -l 50
python3 forreddit_to_cast.py
```
  - arguments: 
    - --sub or -s: for choosing your sub. ex memes or highqualitymemes
    - --limit or -l: for choosing the limit of images that are downloaded ex 10,50,100,...
    - NOTE: Arguments can be run separately, default values will be used for either 
    - default values are:
        - sub: memes
        - limit: 5
