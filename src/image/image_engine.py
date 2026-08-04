import requests
import os
import random


IMAGE_FOLDER = "output/images"


def create_image_folder():

    os.makedirs(
        IMAGE_FOLDER,
        exist_ok=True
    )



def download_image(keyword, filename):

    create_image_folder()


    url = (
        "https://source.unsplash.com/"
        "1080x1920/?"
        + keyword
    )


    try:

        response = requests.get(
            url,
            timeout=20
        )


        path = (
            f"{IMAGE_FOLDER}/"
            f"{filename}.jpg"
        )


        with open(
            path,
            "wb"
        ) as file:

            file.write(
                response.content
            )


        return path


    except Exception:


        return create_default_image(
            filename
        )



def create_default_image(filename):

    from PIL import Image


    path = (
        f"{IMAGE_FOLDER}/"
        f"{filename}.jpg"
    )


    img = Image.new(
        "RGB",
        (1080,1920),
        (30,30,30)
    )


    img.save(path)


    return path
