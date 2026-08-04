import requests
import os


IMAGE_FOLDER = "output/images"


def create_image_folder():

    os.makedirs(
        IMAGE_FOLDER,
        exist_ok=True
    )



def download_image(keyword, filename):

    create_image_folder()

    path = (
        f"{IMAGE_FOLDER}/"
        f"{filename}.jpg"
    )


    # Use a reliable placeholder image
    url = "https://picsum.photos/1080/1920"


    try:

        response = requests.get(
            url,
            timeout=30
        )


        with open(
            path,
            "wb"
        ) as file:

            file.write(
                response.content
            )


        print(
            "Image created:",
            path
        )


        return path


    except Exception as e:

        print(
            "Image error:",
            e
        )

        return None
