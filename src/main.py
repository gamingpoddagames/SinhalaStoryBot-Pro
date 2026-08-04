import json
from src.story.story_engine import create_story
from src.video.video_builder import create_video


def load_config():

    with open(
        "config/settings.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def start_bot():

    config = load_config()

    print("==============================")
    print(" SinhalaStoryBot Pro Started ")
    print("==============================")


    for number in range(config["videos_per_day"]):

        print(
            f"Creating Video {number+1}/{config['videos_per_day']}"
        )

        story = create_story()

        create_video(
            story,
            number+1,
            config
        )


    print("All videos completed")
