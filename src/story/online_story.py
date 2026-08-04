import requests
import random


STORIES = [

"""
A poor farmer found a mysterious old box under a tree.
Inside the box was a letter from his grandfather.
The letter revealed a forgotten family secret.
The farmer searched for the truth and discovered
that kindness from the past changed his future.
""",


"""
A lonely fisherman saw a strange light near the ocean.
He followed the light and found an old boat.
Inside the boat was a diary telling a forgotten story.
He returned the diary to its owner after many years.
""",


"""
A little village had an abandoned house.
Everyone was afraid to enter it.
One day a young boy entered the house
and discovered not a ghost,
but a beautiful memory hidden inside.
"""
]



def get_online_story():

    story=random.choice(STORIES)


    return {

        "title":
        "අභිරහස් කතාව",

        "content":
        story

    }
