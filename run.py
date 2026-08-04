import os
from src.main import start_bot

if __name__ == "__main__":

    folders = [
        "output/videos",
        "output/images",
        "output/audio",
        "output/temp",
        "logs",
        "database"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    start_bot()
