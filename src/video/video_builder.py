from moviepy import *
import os

from src.audio.tts_engine import create_voice
from src.subtitle.scrolling_text import create_text_image
from src.image.image_engine import download_image
from src.upload.metadata import create_metadata
from src.upload.queue import add_to_queue


def create_video(story, number, config):

    title = story["title"]
    text = story["content"]

    print("Rendering:", title)


    # Background image
    image_path = download_image(
        title,
        f"background_{number}"
    )


    # Sinhala voice
    audio_path = create_voice(
        text,
        f"voice_{number}"
    )


    # Subtitle image
    text_image = create_text_image(
        text,
        f"text_{number}"
    )


    duration = 15


    # Create background video
    background = ImageClip(
        image_path
    ).resized(
        (
            config["video_width"],
            config["video_height"]
        )
    ).with_duration(duration)



    # Add text layer
    subtitle = ImageClip(
        text_image
    ).with_duration(duration)



    video = CompositeVideoClip(
        [
            background,
            subtitle
        ]
    )


    # Add audio
    voice = AudioFileClip(
        audio_path
    )

    video = video.with_audio(
        voice
    )


    os.makedirs(
        config["output_folder"],
        exist_ok=True
    )


    output = (
        f"{config['output_folder']}/"
        f"story_{number}.mp4"
    )


    print("Exporting video...")


    video.write_videofile(
        output,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        preset="ultrafast"
    )


    metadata = create_metadata(
        title
    )


    add_to_queue(
        output,
        metadata
    )


    print(
        "Saved:",
        output
    )
