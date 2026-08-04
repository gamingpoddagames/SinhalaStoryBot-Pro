from database.database import story_exists


def check_duplicate(story):

    if story_exists(story):

        return True

    return False
