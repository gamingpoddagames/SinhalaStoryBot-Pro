from PIL import Image, ImageDraw, ImageFont
import os


def get_font(size):

    fonts = [
        "/usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf",
        "/usr/share/fonts/opentype/noto/NotoSansSinhala-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    ]

    for font in fonts:
        if os.path.exists(font):
            return ImageFont.truetype(
                font,
                size
            )

    return ImageFont.load_default()



def create_text_image(
        text,
        filename,
        width=1080,
        height=1920):


    os.makedirs(
        "output/temp",
        exist_ok=True
    )


    image = Image.new(
        "RGBA",
        (
            width,
            height
        ),
        (
            0,
            0,
            0,
            0
        )
    )


    draw = ImageDraw.Draw(
        image
    )


    font = get_font(85)



    # Take only first lines
    words = text.split()



    y = 1400


    line = ""


    for word in words[:12]:

        if len(line + word) < 20:

            line += word + " "

        else:

            draw.text(
                (
                    80,
                    y
                ),
                line,
                font=font,
                fill=(255,255,255,255),
                stroke_width=3,
                stroke_fill=(0,0,0,255)
            )

            y += 120

            line = word + " "



    if line:

        draw.text(
            (
                80,
                y
            ),
            line,
            font=font,
            fill=(255,255,0,255),
            stroke_width=3,
            stroke_fill=(0,0,0,255)
        )



    path = (
        "output/temp/"
        + filename
        + ".png"
    )


    image.save(
        path
    )


    return path
