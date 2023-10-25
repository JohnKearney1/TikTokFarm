from moviepy.editor import VideoFileClip
from pytube import YouTube
import argparse
import os


def get_next_clip_number(output_folder):
    existing_clips = [file for file in os.listdir(output_folder) if file.startswith("clip_")]
    if not existing_clips:
        return 1
    clip_numbers = [int(clip.split("_")[1].split(".")[0]) for clip in existing_clips]
    next_clip_number = max(clip_numbers) + 1
    return next_clip_number


def split_video(input_video_path, output_folder, clip_length):
    video_clip = VideoFileClip(input_video_path)
    video_duration = video_clip.duration
    num_clips = int(video_duration // clip_length)
    next_clip_number = get_next_clip_number(output_folder)
    for i in range(num_clips):
        start_time = i * clip_length
        end_time = (i + 1) * clip_length
        subclip = video_clip.subclip(start_time, end_time)
        output_path = os.path.join(output_folder, f"clip_{next_clip_number}.mp4")
        next_clip_number += 1
        subclip.write_videofile(output_path, codec="libx264")
    video_clip.close()


def download_youtube_video(video_url, output_folder="unclipped_videos"):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        downloaded_file_path = video_stream.download(output_path=output_folder)
        print(f"Download completed! Video saved at: {downloaded_file_path}")
        return downloaded_file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download and split a YouTube video.')
    parser.add_argument('video_url', help='URL of the YouTube video')
    parser.add_argument('clip_length', type=int, help='Length in seconds of each clipped video')
    args = parser.parse_args()

    downloaded_video_path = download_youtube_video(args.video_url)

    if downloaded_video_path:
        video_output_folder = "clipped_videos"
        split_video(downloaded_video_path, video_output_folder, args.clip_length)
    else:
        print("Video download failed.")
