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


    # Create background image
    image_path = download_image(
        title,
        f"background_{number}"
    )


    # Create Sinhala voice
    audio_path = create_voice(
        text,
        f"voice_{number}"
    )


    # Create subtitle image
    text_image = create_text_image(
        text,
        f"text_{number}"
    )


    # Background video
    background = ImageClip(
        image_path
    ).resized(
        (
            config["video_width"],
            config["video_height"]
        )
    ).with_duration(60)



    # Subtitle layer
    subtitle = ImageClip(
        text_image
    ).with_duration(60)



    # Combine layers
    video = CompositeVideoClip(
        [
            background,
            subtitle
        ]
    )


    # Add voice
    voice = AudioFileClip(
        audio_path
    )

    video = video.with_audio(
        voice
    )


    # Output file
    os.makedirs(
        config["output_folder"],
        exist_ok=True
    )


    output = (
        f"{config['output_folder']}/"
        f"story_{number}.mp4"
    )


 video.write_videofile(
    output,
    fps=24,
    codec="libx264",
    audio_codec="aac",
    preset="ultrafast"
)


    # Add upload queue
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
