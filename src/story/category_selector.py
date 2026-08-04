import random


categories = [

    "ආදර කතාවක්",
    "පවුල් කතාවක්",
    "ගමේ සිදුවීමක්",
    "අභිරහස් කතාවක්",
    "හදවතට දැනෙන කතාවක්",
    "ජීවිත පාඩමක්",
    "භයානක සිදුවීමක්"

]


def get_category():

    return random.choice(categories)
