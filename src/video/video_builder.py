from moviepy import *
import os

from src.audio.tts_engine import create_voice
from src.subtitle.scrolling_text import create_text_image
from src.image.image_engine import download_image


def create_video(story, number, config):

    title = story["title"]
    text = story["content"]


    print("Creating:", title)


    duration = 60


    # create image based on story
    image_path = download_image(
        title,
        f"scene_{number}"
    )


    # create voice
    audio_path = create_voice(
        text,
        f"voice_{number}"
    )


    # create scrolling text
    text_path = create_text_image(
        text,
        f"scroll_{number}"
    )


    background = (
        ImageClip(image_path)
        .resized(
            (
                1080,
                1920
            )
        )
        .with_duration(duration)
    )


    # slow zoom effect

    background = background.resized(
        lambda t:
        1 + (0.05*t)
    )


    subtitle = (
        ImageClip(text_path)
        .with_duration(duration)
        .with_position(
            lambda t:
            (
                "center",
                1800-(t*50)
            )
        )
    )


    video = CompositeVideoClip(
        [
            background,
            subtitle
        ]
    )


    audio = AudioFileClip(
        audio_path
    )


    video = video.with_audio(
        audio
    )


    os.makedirs(
        "output/videos",
        exist_ok=True
    )


    output = (
        "output/videos/"
        f"story_{number}.mp4"
    )


    video.write_videofile(
        output,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        preset="medium"
    )


    print(
        "DONE:",
        output
    )
