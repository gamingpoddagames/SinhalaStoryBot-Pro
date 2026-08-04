from PIL import Image, ImageDraw, ImageFont
import os


def get_font(size):

    fonts = [
        "/usr/share/fonts/opentype/noto/NotoSansSinhala-Regular.ttf",
        "/usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf"
    ]

    for f in fonts:
        if os.path.exists(f):
            return ImageFont.truetype(f,size)

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


    font = get_font(55)



    # split text into smaller parts

    words = text.split()


    lines=[]

    current=""


    for word in words:

        if len(current + word) < 22:

            current += word + " "

        else:

            lines.append(current)

            current = word + " "


    if current:
        lines.append(current)



    # show more lines

    y=550


    for line in lines[:10]:

        box = draw.textbbox(
            (0,0),
            line,
            font=font
        )

        x=(width-(box[2]-box[0]))//2


        draw.text(
            (x,y),
            line,
            font=font,
            fill="white",
            stroke_width=3,
            stroke_fill="black"
        )


        y+=90



    path=f"output/temp/{filename}.png"


    img.save(path)


    return path
