import random


hashtags = [

    "#SinhalaStory",
    "#SinhalaKatha",
    "#SriLanka",
    "#StoryTime",
    "#LifeLessons",
    "#ViralStories",
    "#EmotionalStory",
    "#TikTokSriLanka",
    "#FacebookReels"

]


def generate_hashtags():

    return " ".join(
        random.sample(
            hashtags,
            5
        )
    )



def create_metadata(title):

    return {

        "title": title,

        "description":
        f"""
        {title}

        Sinhala original story ❤️

        Follow for more stories.

        """,

        "hashtags":
        generate_hashtags()

    }
