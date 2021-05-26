#!usr/bin/env/python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

from uploader.configed_parser import ConfigedParser
from uploader.constant import *
import requests
import os
import json


class UploaderException(BaseException):
    pass


class GyazoUploader:
    def __init__(self, parser: ConfigedParser):
        self.__parser: ConfigedParser = parser
        self.__access_token: str = ""
        self.__files_to_upload: list = []

    def run(self) -> None:
        username: str = self.__parser.get_args().get('u')
        self.__valid_credentials(username)
        directory: str = self.__parser.get_args().get('dir')
        self.__upload(directory)

    def __valid_credentials(self, username: str) -> None:
        """Checks if user is save in .gyazo file. If he is, access token is fetched from file. If not, user
        is asked to type so, and then his login and access token is appended to file"""
        try:
            with open(CONFIG_PATH, 'r+') as config_file:
                data: dict = json.load(config_file)
                for key, value in data.items():
                    if key == username:
                        for nd_key, nd_value in value.items():
                            if nd_key == "access_token":
                                self.__access_token = nd_value
                                return

                self.__access_token: str = input("It is your first time here. Type in your access token: ")
                json_to_append: dict = {username: {"access_token": self.__access_token}}
                data.update(json_to_append)
                config_file.seek(0)
                json.dump(data, config_file)
        except FileNotFoundError:
            with open(CONFIG_PATH, 'w+') as config_file:
                config_file.write("{}")
            self.__valid_credentials(username)

    def __upload(self, directory: str) -> None:
        """list all paths to files, with extension .png, .jpg, in indicated directory then executes method
        <code> upload_image </code> for each"""
        try:
            dir_content: list = os.listdir(directory)
            for element in dir_content:
                if element.endswith(".jpg") or element.endswith(".png"):
                    self.__files_to_upload.append(directory + "\\" + element)
            print(self.__files_to_upload)
        except FileNotFoundError as e:
            raise UploaderException("Incorrect dir: {}".format(str(e)))

        for file_path in self.__files_to_upload:
            self.__upload_image(file_path)

    def __upload_image(self, path_to_file: str) -> None:
        """ Parameters
        ----------
        path_to_file : str, required
            Path to file to upload"""
        try:
            with open(path_to_file, 'rb') as f:
                r = requests.request('post', UPLOAD_URL, files={'imagedata': f}, headers={
                    'Authorization': 'Bearer ' + self.__access_token})
                if r.status_code == 200:
                    print("Image {} uploaded".format(path_to_file))
                else:
                    raise UploaderException
        except FileNotFoundError as e:
            raise UploaderException("Incorrect file path: {}".format(str(e)))
