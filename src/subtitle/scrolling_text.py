from PIL import Image, ImageDraw, ImageFont
import os
import textwrap


def get_font(size):

    fonts = [

        "/usr/share/fonts/opentype/noto/NotoSansSinhala-Regular.ttf",

        "/usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf",

        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    ]


    for font in fonts:

        if os.path.exists(font):

            return ImageFont.truetype(
                font,
                size
            )


    return ImageFont.load_default()



def create_text_image(text, filename):


    os.makedirs(
        "output/temp",
        exist_ok=True
    )


    width = 1080
    height = 1920


    img = Image.new(
        "RGBA",
        (width,height),
        (0,0,0,0)
    )


    draw = ImageDraw.Draw(img)


    # smaller but clear text

    font = get_font(65)



    # split Sinhala text into lines

    lines = []


    for paragraph in text.split("\n"):

        wrapped = textwrap.wrap(
            paragraph,
            width=18
        )

        lines.extend(
            wrapped
        )



    # center alignment

    y = 700


    for line in lines:


        box = draw.textbbox(
            (0,0),
            line,
            font=font
        )


        text_width = (
            box[2]-box[0]
        )


        x = (
            width-text_width
        )//2



        # shadow

        draw.text(

            (
                x+4,
                y+4
            ),

            line,

            font=font,

            fill=(0,0,0,220)

        )



        # main text

        draw.text(

            (
                x,
                y
            ),

            line,

            font=font,

            fill=(255,255,255,255),

            stroke_width=2,

            stroke_fill=(0,0,0,255)

        )


        y += 100



    path = (

        "output/temp/"

        + filename

        + ".png"

    )


    img.save(
        path
    )


    return path
