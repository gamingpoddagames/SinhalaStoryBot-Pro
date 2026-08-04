import json
import os


QUEUE_FILE = "database/upload_queue.json"



def add_to_queue(video, metadata):

    os.makedirs(
        "database",
        exist_ok=True
    )


    if os.path.exists(QUEUE_FILE):

        with open(
            QUEUE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

    else:

        data = []


    data.append({

        "video": video,

        "metadata": metadata,

        "uploaded": False

    })


    with open(
        QUEUE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )
