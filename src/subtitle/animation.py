from moviepy import *


def scroll_text(clip, duration):

    height = clip.h


    return clip.with_position(
        lambda t: (
            "center",
            height - (t * 80)
        )
    ).with_duration(duration)



def fade_in(clip):

    return clip.fadein(1)



def fade_out(clip):

    return clip.fadeout(1)
