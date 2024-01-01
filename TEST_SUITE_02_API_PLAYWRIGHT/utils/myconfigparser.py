"""Reads ini files in config folder"""

import configparser
from pathlib import Path

CG_FILE = "petsqa.ini"
CG_FILE_DIR = "config"
# cg_fileFlaskApp = "qa.ini"

config = configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(CG_FILE_DIR).joinpath(CG_FILE)


config.read(CONFIG_FILE)


def get_pet_api_url():
    """GET"""
    return config["pet"]["url"]


print(get_pet_api_url())
