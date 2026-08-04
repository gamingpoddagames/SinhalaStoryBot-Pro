from PIL import Image, ImageDraw, ImageFont
import os


def create_text_image(
        text,
        filename,
        width=1080,
        height=2000):


    os.makedirs(
        "output/temp",
        exist_ok=True
    )


    img = Image.new(
        "RGBA",
        (width,height),
        (0,0,0,0)
    )


    draw = ImageDraw.Draw(img)


    font = ImageFont.load_default()


    y = 100


    for line in text.split("\n"):

        draw.text(
            (50,y),
            line,
            font=font,
            fill="white"
        )

        y += 80



    path = (
        "output/temp/"
        + filename
        + ".png"
    )


    img.save(path)


    print(
        "Subtitle created:",
        path
    )


    return path
