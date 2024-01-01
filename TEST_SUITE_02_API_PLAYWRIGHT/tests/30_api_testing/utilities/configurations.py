import configparser

from boxen import bx_info, bx_result


def getConfig():
    config = configparser.ConfigParser()
    config.read("./properties.ini")
    return config


connect_config = {
    "user": getConfig()["SQL"]["user"],
    "password": getConfig()["SQL"]["password"],
    "host": getConfig()["SQL"]["host"],
    "database": getConfig()["SQL"]["database"],
}

bx_info(getConfig()["SQL"]["user"])
bx_info(str(connect_config))
