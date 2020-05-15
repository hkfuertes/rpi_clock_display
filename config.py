import yaml
import os

config_file = os.path.join(os.path.dirname(__file__), './config.yml')


class Config:

    __instance = None

    @staticmethod
    def read_config():
        instance = None
        with open(config_file, 'r') as stream:
            try:
                instance = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return instance

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Config.__instance == None:
            Config()
        return Config.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Config.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Config.__instance = Config.read_config()
