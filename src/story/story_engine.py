import random

from src.story.category_selector import get_category
from src.story.duplicate_checker import check_duplicate

from database.database import (
    create_database,
    save_story
)



def generate_story():


    category = get_category()


    stories = [

        {
        "title":"අම්මාගේ ආදරය",
        "text":
        """
        කුඩා ගමක ජීවත් වූ සෙනුරට
        අම්මා හැමදාම ශක්තියක් වුණා.

        දුෂ්කර කාලවලදී පවා
        ඇය තම පුතා වෙනුවෙන්
        සියල්ල කැප කළා.

        අවසානයේ සෙනුර සාර්ථක වී
        අම්මාට සතුටු ජීවිතයක් ලබා දුන්නා.
        """
        },


        {
        "title":"අවංක මිනිසා",
        "text":
        """
        එක් දිනක ගමේ මිනිසෙකුට
        විශාල මුදලක් හමු වුණා.

        ඔහුට එය තබාගන්න හැකි වුණත්
        ඔහු සැබෑ අයිතිකරු සොයා ගියා.

        ඔහුගේ අවංකභාවය නිසා
        මුළු ගමම ඔහුට ගරු කළා.
        """
        },


        {
        "title":"පරණ නිවසේ රහස",
        "text":
        """
        ගමේ පැරණි නිවසක් ගැන
        අමුතු කතා පැතිරුණා.

        එක් රාත්‍රියක තරුණයෙක්
        එහි ඇතුළට ගියා.

        එහි තිබූ රහස
        සියල්ලන්ම පුදුමයට පත් කළා.
        """
        }

    ]


    story = random.choice(stories)


    return story["title"], story["text"]



def create_story():

    create_database()


    while True:


        title, text = generate_story()


        if not check_duplicate(text):

            save_story(title,text)


            return {

                "title": title,
                "content": text

            }
