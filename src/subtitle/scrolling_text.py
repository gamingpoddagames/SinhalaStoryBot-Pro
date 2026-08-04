from PIL import Image, ImageDraw, ImageFont
import os


def get_font(size):

    fonts = [

        "/usr/share/fonts/opentype/noto/NotoSansSinhala-Regular.ttf",

        "/usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf",

        "/usr/share/fonts/truetype/lklug/LKLUG.ttf",

        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    ]


    for font in fonts:

        if os.path.exists(font):

            return ImageFont.truetype(
                font,
                size
            )


    return ImageFont.load_default()



def split_text(text, words_per_page=25):

    words = text.replace(
        "\n",
        " "
    ).split()


    pages = []


    current = []


    for word in words:


        current.append(word)


        if len(current) >= words_per_page:

            pages.append(
                " ".join(current)
            )

            current = []


    if current:

        pages.append(
            " ".join(current)
        )


    return pages




def create_single_page(text, filename):


    os.makedirs(
        "output/temp",
        exist_ok=True
    )


    width = 1080
    height = 1920


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


    font = get_font(
        65
    )


    words = text.split()


    lines = []

    line = ""


    for word in words:


        test = line + " " + word


        if len(test) < 20:

            line = test

        else:

            lines.append(
                line
            )

            line = word



    if line:

        lines.append(
            line
        )



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
            width - text_width
        ) // 2



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

            stroke_width=3,

            stroke_fill=(0,0,0,255)

        )


        y += 100



    path = (

        "output/temp/"

        + filename

        + ".png"

    )


    image.save(
        path
    )


    return path




def create_text_pages(text, filename):


    pages = split_text(
        text
    )


    results = []


    for index, page in enumerate(pages):


        file = create_single_page(

            page,

            f"{filename}_{index}"

        )


        results.append(
            file
        )


    return results




# Compatibility with old video_builder.py

def create_text_image(text, filename):


    pages = create_text_pages(

        text,

        filename

    )


    return pages[0]
