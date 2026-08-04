from moviepy import *


def create_intro():

    return TextClip(
        text="❤️ Sinhala Stories",
        font_size=80,
        color="white"
    ).with_duration(3)



def create_outro():

    return TextClip(
        text="Follow for more stories ❤️",
        font_size=60,
        color="white"
    ).with_duration(3)
