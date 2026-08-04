from moviepy import *
import os

from src.audio.tts_engine import create_voice
from src.subtitle.scrolling_text import create_text_image
from src.image.image_engine import download_image

try:
    from src.upload.telegram import send_video
except:
    send_video = None



def create_video(story, number, config):

    title = story["title"]
    text = story["content"]


    print("Creating:", title)


    # Create image

    image_path = download_image(
        title,
        f"scene_{number}"
    )


    if image_path is None:

        print("Image missing")

        return



    # Create voice

    audio_path = create_voice(
        text,
        f"voice_{number}"
    )


    audio = AudioFileClip(
        audio_path
    )


    duration = audio.duration



    # Background image

    background = ImageClip(
        image_path
    )


    background = (
        background
        .resized(
            (
                1080,
                1920
            )
        )
        .with_duration(
            duration
        )
    )



    # Subtitle image

    subtitle_path = create_text_image(
        text,
        f"subtitle_{number}"
    )


    subtitle = ImageClip(
        subtitle_path
    )


    subtitle = (
        subtitle
        .with_duration(
            duration
        )
        .with_position(
            lambda t:
            (
                "center",
                500 - (t * 30)
            )
        )
    )



    # Combine layers

    video = CompositeVideoClip(
        [
            background,
            subtitle
        ],
        size=(
            1080,
            1920
        )
    )


    video = video.with_audio(
        audio
    )



    # Save

    os.makedirs(
        "output/videos",
        exist_ok=True
    )


    output = (
        "output/videos/"
        f"story_{number}.mp4"
    )


    print("Rendering video...")


    video.write_videofile(
        output,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        preset="medium"
    )



    print(
        "Video saved:",
        output
    )



    # Telegram

    if send_video:

        try:

            send_video(
                output
            )

        except Exception as e:

            print(
                "Telegram error:",
                e
            )
