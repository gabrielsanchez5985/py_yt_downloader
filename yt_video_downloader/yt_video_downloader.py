#!/usr/bin/env python3

from pytube.__main__ import YouTube
from pytube.exceptions import PytubeError
import os
import argparse

def download_yt_video(url, destination_folder):
    os.chdir(destination_folder)

    try:
        yt = YouTube(url)
    except PytubeError as err:
        print(f"Unknown error. Video unavailable. Reason: {err}")
    else:
        yt.streams.get_highest_resolution().download()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Youtube video")
    parser.add_argument(
            "-u", "--url",
            metavar="Youtube URL", 
            type=str, 
            help="The Youtube video URL.",
        )
    parser.add_argument(
            "-d", "--dir",
            metavar="Directory path",
            type=str,
            help="The directory path where to download the file.",
        )
    args = parser.parse_args()


    download_yt_video(args.url, args.dir)