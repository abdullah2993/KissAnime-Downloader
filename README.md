# KissAnime Downloader [![Build Status](https://travis-ci.org/Abdullah2993/KissAnime-Downloader.svg?branch=master)](https://travis-ci.org/Abdullah2993/KissAnime-Downloader)
A python script that lets you download anime episodes from KissAnime
## Usage
```
usage: kissanime_dl.py [-h] (-l LINK | -n NAME) [-q {360p,480p,720p,1080p}]
                       [-v] [-e EPISODES [EPISODES ...]]

Download anime from KissAnime.to

optional arguments:
  -h, --help            show this help message and exit
  -l LINK, --link LINK  Link to Anime
  -n NAME, --name NAME  Name of the anime
  -q {360p,480p,720p,1080p}, --quality {360p,480p,720p,1080p}
                        Video Quality
  -v, --verbose
  -e EPISODES [EPISODES ...], --episodes EPISODES [EPISODES ...]
```

## Run from source
Clone the repository

`git clone git@github.com:Abdullah2993/KissAnime-Downloader.git`

Install dependencies

`pip install -r Requiments.txt`

Run

`kissanime_dl.py`

