from moviepy import *
import os

from src.audio.tts_engine import create_voice
from src.subtitle.scrolling_text import create_text_image
from src.image.image_engine import download_image


def create_video(story, number, config):

    title = story["title"]
    text = story["content"]

    print("==============================")
    print("Creating Video:", title)
    print("==============================")


    # -----------------------------
    # Create background image
    # -----------------------------

    image_path = download_image(
        title,
        f"scene_{number}"
    )


    if image_path is None:
        print("Image creation failed")
        return



    # -----------------------------
    # Create Sinhala voice
    # -----------------------------

    audio_path = create_voice(
        text,
        f"voice_{number}"
    )


    audio = AudioFileClip(
        audio_path
    )


    duration = audio.duration + 2


    print(
        "Video duration:",
        duration
    )



    # -----------------------------
    # Background video
    # -----------------------------

    background = ImageClip(
        image_path
    )


    background = (
        background
        .resized(
            (
                config["video_width"],
                config["video_height"]
            )
        )
        .with_duration(duration)
    )


    # Slow zoom effect

    background = background.resized(
        lambda t:
        1 + (0.03*t)
    )



    # Center crop after zoom

    background = background.with_position(
        ("center","center")
    )



    # -----------------------------
    # Sinhala scrolling text
    # -----------------------------

    text_image = create_text_image(
        text,
        f"subtitle_{number}"
    )

subtitle = ImageClip(
    text_image
).resized(
    1.2
)


    subtitle = (
        subtitle
        .with_duration(duration)
        .with_position(
            lambda t:
            (
                "center",
                1800 - (t * 70)
            )
        )
    )



    # -----------------------------
    # Combine video layers
    # -----------------------------

    video = CompositeVideoClip(
        [
            background,
            subtitle
        ],
        size=(
            config["video_width"],
            config["video_height"]
        )
    )



    # Add voice

    video = video.with_audio(
        audio
    )



    # -----------------------------
    # Save
    # -----------------------------

    os.makedirs(
        "output/videos",
        exist_ok=True
    )


    output = (
        "output/videos/"
        f"story_{number}.mp4"
    )


    print(
        "Rendering..."
    )


    video.write_videofile(
        output,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        preset="medium"
    )


    print(
        "Completed:",
        output
    )
