from moviepy import *

import os

from src.audio.tts_engine import create_voice
from src.subtitle.scrolling_text import create_text_image
from src.image.image_engine import download_image



def create_video(
        story,
        number,
        config):


    title = story["title"]

    text = story["content"]


    print(
        "Rendering:",
        title
    )


    image = create_text_image(
        text,
        f"text_{number}"
    )


    audio = create_voice(
        text,
        f"voice_{number}"
    )


    background = ColorClip(
        size=(
            config["video_width"],
            config["video_height"]
        ),
        color=(20,20,20),
        duration=60
    )


    subtitle = ImageClip(
        image
    ).with_duration(60)



    video = CompositeVideoClip(
        [
            background,
            subtitle
        ]
    )


    voice = AudioFileClip(
        audio
    )


    video = video.with_audio(
        voice
    )



    output = (
        f"{config['output_folder']}/"
        f"story_{number}.mp4"
    )


    os.makedirs(
        config["output_folder"],
        exist_ok=True
    )



    video.write_videofile(
        output,
        fps=config["fps"],
        codec="libx264",
        audio_codec="aac"
    )


    print(
        "Saved:",
        output
    )
