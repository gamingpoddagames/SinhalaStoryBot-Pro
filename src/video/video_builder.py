from moviepy import *
import os

from src.audio.tts_engine import create_voice
from src.subtitle.scrolling_text import create_text_image
from src.image.image_engine import download_image
from src.upload.telegram import send_video



def create_video(story, number, config):

    title = story["title"]
    text = story["content"]


    print("Creating:", title)


    # IMAGE

    image_path = download_image(
        title,
        f"scene_{number}"
    )


    # VOICE

    audio_path = create_voice(
        text,
        f"voice_{number}"
    )


    audio = AudioFileClip(
        audio_path
    )


    duration = audio.duration + 1



    # BACKGROUND

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



    # ADD DARK OVERLAY
    # makes text readable

    dark = ColorClip(
        size=(1080,1920),
        color=(0,0,0),
        duration=duration
    )

    dark = dark.with_opacity(
        0.25
    )



    # SUBTITLE IMAGE

    subtitle_path = create_text_image(
        text,
        f"subtitle_{number}"
    )


    subtitle = ImageClip(
        subtitle_path
    )


   subtitle = (
    subtitle
    .with_duration(duration)
    .with_position(
        lambda t:
        (
            "center",
            500 - (t*30)
        )
    )
)



    video = CompositeVideoClip(
        [
            background,
            dark,
            subtitle
        ],

        size=(1080,1920)

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



    print("Rendering...")


    video.write_videofile(

        output,

        fps=30,

        codec="libx264",

        audio_codec="aac",

        preset="medium"

    )


    print(
        "Created:",
        output
    )


    try:

        send_video(output)

    except:

        pass
