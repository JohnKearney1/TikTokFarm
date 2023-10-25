import os
import schedule
import time
from tiktok_uploader.upload import upload_video

# Path to the directory containing the clipped videos
video_directory = "clipped_videos"

# Path to the directory where posted videos will be moved
posted_video_directory = "posted_videos"


# Function to post a video on TikTok
def post_video():
    # Get a list of video files in the video directory without the .mp4 extension
    video_files = [file for file in os.listdir(video_directory) if file.lower().endswith('.mp4')]

    # Filter video files that match the naming scheme "clip_n"
    valid_video_files = [file for file in video_files if file.startswith("clip_")]

    if valid_video_files:
        # Extract the 'n' values from the video file names and find the smallest 'n'
        n_values = [int(file.split("_")[1].split(".")[0]) for file in valid_video_files]
        smallest_n = min(n_values)

        # Construct the file name of the video with the smallest 'n' without the .mp4 extension
        video_to_post = os.path.join(video_directory, f"clip_{smallest_n}.mp4")

        print(f"Found video to post: {video_to_post}")

        # Upload the video to TikTok
        upload_video(video_to_post, description="#fyp", cookies="cookies.txt", comment=True, stitch=True, duet=True)
        print(f"Posted video: {video_to_post}")

        # Move the posted video file to the posted_videos folder
        posted_video_path = os.path.join(posted_video_directory, os.path.basename(video_to_post))
        os.rename(video_to_post, posted_video_path)
        print(f"Moved video to posted_videos folder: {posted_video_path}")
    else:
        print("No valid videos found to post.")


if __name__ == '__main__':
    # Run post_video once at startup
    post_video()

    # Schedule post_video to run every 30 minutes
    schedule.every(30).minutes.do(post_video)

    # Run the scheduled tasks
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} > Running Scheduled Tasks")
        schedule.run_pending()
        time.sleep(1)
