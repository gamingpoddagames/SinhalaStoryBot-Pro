import requests
import os


def send_video(video_path):

    token = os.getenv(
        "TELEGRAM_BOT_TOKEN"
    )

    chat_id = os.getenv(
        "TELEGRAM_CHAT_ID"
    )


    if not token or not chat_id:

        print(
            "Telegram settings missing"
        )

        return False



    url = (
        "https://api.telegram.org/"
        f"bot{token}/sendVideo"
    )


    try:

        with open(
            video_path,
            "rb"
        ) as video:


            response = requests.post(

                url,

                data={

                    "chat_id": chat_id,

                    "caption":
                    "❤️ Sinhala Story Video"

                },

                files={

                    "video": video

                }

            )


        if response.status_code == 200:

            print(
                "Telegram upload completed"
            )

            return True


        else:

            print(
                response.text
            )

            return False



    except Exception as e:

        print(
            "Telegram error:",
            e
        )

        return False
