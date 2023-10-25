# TikTokFarm

This is a basic python script that helps automate the downloading, segmentation,
and cross-posting of YouTube videos to TikTok accounts. 

## Setup

```commandline
git clone https://github.com/JohnKearney1/TikTokFarm
cd TikTokFarm
pip install -r requirements.txt
```

## Usage

### main.py

There are two python files you will use in tandem. 
The first file main.py, downloads and locates the files appropriately.
Essentially, an ingestion script. 

Syntax:
```commandline
python main.py <"YouTube Video URL"> <Clip Duration (seconds)>
```

Example: The following command will download the video and segment it into multiple 30 second clips.
```commandline
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 30
```

### uploader.py
The second script uploader.py, runs continuously, and posts the ingested videos to a TikTok account
on a given schedule defined in minutes.