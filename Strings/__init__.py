import os
from typing import List

import yaml

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[languages]


for filename in os.listdir(r"./Strings/languages/"):
    if "english" not in languages:
        languages["english"] = yaml.safe_load(
            open(r"./Strings/languages/english.yml", encoding="utf8")
        )
        languages_present["english"] = languages["english"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "english":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./Strings/languages/" + filename, encoding="utf8")
        )
        for item in languages["english"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["english"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("There is some issue with the language file inside bot.")
        exit()
