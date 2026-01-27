import os
import random
import string
from datetime import datetime
from pathlib import Path

#-----------------------------------------------------
#Helpers
#-----------------------------------------------------
def ensure_dirs() -> None:
    #Create output directories if they don't exist.
    Path("Memorable").mkdir(parents=True, exist_ok=True)
    Path("Random").mkdir(parents=True, exist_ok=True)

def timestamp_str() -> str:
    #Return a readable timestamp including day, date,and time.
    return datetime.now().strftime("%a, %b %d %Y %I:%N:%S %p")

def append_to_file(folder: str, password: str) -> None:
    #Append password and timestamp to the correct Generated_Passwords.txt file.
    ensure_dirs()
    out_path = Path(folder) / "Generated_Passwords.txt"
    with out_path.open("a", encoding="utf-8") as f:
        f.write(f"{timestamp_str()} | {password}\n")

def load_words(filepath: str) -> list[str]:
    #Load words from the nouns file.
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(
            f"Missing word list: {filepath}\n"
            "Download top_english_nouns_lower_100000.txt and place it in the project folder."
        )
    with path.open("r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    if not words:
        raise ValueError("Word list file is empty.")
    return words
