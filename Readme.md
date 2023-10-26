# TikTokFarm
![](readmelogo.png)

This is a basic python script that helps automate the downloading, segmentation,
and cross-posting of YouTube videos to TikTok accounts. 

## Setup

```commandline
git clone https://github.com/JohnKearney1/TikTokFarm
cd TikTokFarm
pip install -r requirements.txt
```

Ensure you have installed Google Chrome on your computer.
The script will spawn a headless browser to upload videos.

The uploader requires your credentials to function, but uses a saved browser cookie
in place of plaintext username and password. Here's how to get your cookie:

1. Install the [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
extension.
2. Go to TikTok.com and login to the account the bot will use.
3. Use the extension to Export As `cookies.txt` to the root folder of this project (TikTokFarm/cookies.txt)

## Usage

There are two python files you will use in tandem. 
The first file **main.py**, downloads and locates the files appropriately.
Essentially, an ingestion script. 

**uploader.py** runs 24/7 in the background and posts a video from the clipped videos
queue every 30 minutes. 

The intended manner of usage is to run the **uploader** script, then use the
**main** script to continually feed new clips to the uploader.

### main.py

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
on a given schedule, set to every 30 minutes by default.

```commandline
python uploader.py
```


### tags.txt
The tags.txt file contains a list of tags that are pulled from when randomly selecting tags for a video. To add your own tags, just add them to the tags.txt file on a new line. Some example tags are provided for you.