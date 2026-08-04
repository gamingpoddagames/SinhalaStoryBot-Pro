import json

from src.story.story_engine import create_story
from src.video.video_builder import create_video

from src.utils.logger import setup_logger



def load_config():

    with open(
        "config/settings.json",
        "r",
        encoding="utf-8"

    ) as f:

        return json.load(f)




def start_bot():


    logger = setup_logger()


    config = load_config()


    logger.info(
        "Bot Started"
    )


    for i in range(
        config["videos_per_day"]
    ):


        try:


            logger.info(
                f"Creating video {i+1}"
            )


            story = create_story()


            create_video(
                story,
                i+1,
                config
            )


            logger.info(
                "Video completed"
            )



        except Exception as e:


            logger.error(
                str(e)
            )


    logger.info(
        "Bot Finished"
    )
