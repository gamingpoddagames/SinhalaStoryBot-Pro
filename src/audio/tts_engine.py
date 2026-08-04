from gtts import gTTS
import os


def create_voice(text, filename):

    os.makedirs(
        "output/audio",
        exist_ok=True
    )

    path = f"output/audio/{filename}.mp3"


    voice = gTTS(
        text=text,
        lang="si"
    )

    voice.save(path)


    return path
