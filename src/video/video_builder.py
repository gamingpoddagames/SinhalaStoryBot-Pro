from moviepy import *
import os

from src.audio.tts_engine import create_voice
from src.subtitle.scrolling_text import create_text_image
from src.image.image_engine import download_image
from src.upload.telegram import send_video



def create_video(story, number, config):

    title = story["title"]
    text = story["content"]


    print("==============================")
    print("Creating:", title)
    print("==============================")


    # -------------------------
    # Create background image
    # -------------------------

    image_path = download_image(
        title,
        f"scene_{number}"
    )


    if not image_path:

        print("Image failed")
        return



    # -------------------------
    # Create Sinhala voice
    # -------------------------

    audio_path = create_voice(
        text,
        f"voice_{number}"
    )


    audio = AudioFileClip(
        audio_path
    )


    duration = audio.duration



    # -------------------------
    # Background video
    # -------------------------

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
        .with_duration(duration)
    )



    # Slow zoom effect

    background = background.resized(
        lambda t:
        1 + (0.02*t)
    )



    # -------------------------
    # Sinhala subtitle
    # -------------------------

    subtitle_path = create_text_image(
        text,
        f"subtitle_{number}"
    )


    subtitle = ImageClip(
        subtitle_path
    )


    subtitle = (
        subtitle
        .resized(
            1.3
        )
        .with_duration(
            duration
        )
        .with_position(
            (
                "center",
                1250
            )
        )
    )



    # -------------------------
    # Combine
    # -------------------------

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



    # -------------------------
    # Save video
    # -------------------------

    os.makedirs(
        "output/videos",
        exist_ok=True
    )


    output = (
        "output/videos/"
        f"story_{number}.mp4"
    )



    print(
        "Rendering video..."
    )


    video.write_videofile(

        output,

        fps=30,

        codec="libx264",

        audio_codec="aac",

        preset="medium"

    )



    print(
        "Video created:",
        output
    )



    # -------------------------
    # Send Telegram
    # -------------------------

    try:

        send_video(
            output
        )

    except Exception as e:

        print(
            "Telegram error:",
            e
        )


    print(
        "Finished"
    )
