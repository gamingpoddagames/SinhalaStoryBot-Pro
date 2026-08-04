from PIL import Image, ImageDraw, ImageFont
import os


def create_text_image(
        text,
        filename,
        width=1080,
        height=1920):


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


    try:

        font = ImageFont.truetype(
            "arial.ttf",
            55
        )

    except:

        font = ImageFont.load_default()



    y = 100


    for line in text.split("\n"):

        draw.text(
            (80,y),
            line,
            font=font,
            fill="white"
        )

        y += 90



    path = f"output/temp/{filename}.png"

    img.save(path)


    return path
