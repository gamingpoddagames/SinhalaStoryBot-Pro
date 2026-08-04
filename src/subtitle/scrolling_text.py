from PIL import Image, ImageDraw, ImageFont
import os


def get_font(size):

    fonts = [
        "/usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf",
        "/usr/share/fonts/opentype/noto/NotoSansSinhala-Regular.ttf",
        "/usr/share/fonts/truetype/lklug/LKLUG.ttf"
    ]

    for f in fonts:
        if os.path.exists(f):
            return ImageFont.truetype(f,size)

    return ImageFont.load_default()



def create_text_pages(text, filename):

    os.makedirs(
        "output/temp",
        exist_ok=True
    )


    sentences = []

    for s in text.replace("\n"," ").split("."):

        if len(s.strip()) > 5:
            sentences.append(
                s.strip()
            )


    pages=[]


    # create multiple subtitle images

    for index in range(0,len(sentences),3):

        page_text="\n".join(
            sentences[index:index+3]
        )


        img=Image.new(
            "RGBA",
            (1080,1920),
            (0,0,0,0)
        )


        draw=ImageDraw.Draw(img)

        font=get_font(65)


        lines=page_text.split("\n")


        y=750


        for line in lines:


            box=draw.textbbox(
                (0,0),
                line,
                font=font
            )


            x=(1080-(box[2]-box[0]))//2


            draw.text(
                (x,y),
                line,
                font=font,
                fill="white",
                stroke_width=4,
                stroke_fill="black"
            )


            y+=120



        path=f"output/temp/{filename}_{len(pages)}.png"


        img.save(path)


        pages.append(path)



    return pages
