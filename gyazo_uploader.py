#!usr/bin/env/python3.9
import sys

from configed_parser import ConfigedParser
import constant
import requests
import os
import json


class GyazoUploader:
    def __init__(self, parser: ConfigedParser):
        self.parser: ConfigedParser = parser
        self.__access_token: str = ""
        self.__files_to_upload: list = []
        self.__save_credentials()
        self.__upload()

    def __save_credentials(self) -> None:
        username: str = self.parser.get_args().get('u')
        try:
            with open(constant.CONFIG_PATH, 'r+') as config_file:
                data: dict = json.load(config_file)
                for key, value in data.items():
                    if key == username:
                        for nd_key, nd_value in value.items():
                            if nd_key == "access_token":
                                self.__access_token = nd_value
                                return

                access_token: str = input("It is your first time here. Type in your access token: ")
                json_to_append: dict = {username: {"access_token": access_token}}
                data.update(json_to_append)
                config_file.seek(0)
                json.dump(data, config_file)
        except FileNotFoundError:
            print("Couldn't localize '.gyazo' file in home catalog")

    def __upload(self) -> None:
        directory: str = self.parser.get_args().get('dir')
        try:
            dir_content = os.listdir(directory)
            for element in dir_content:
                if element.endswith(".jpg") or element.endswith(".png"):
                    self.__files_to_upload.append(element)
            print(self.__files_to_upload)
        except FileNotFoundError:
            print("System can't find this directory!")
            sys.exit(0)
        for file_path in self.__files_to_upload:
            self.__upload_image(file_path)

    def __upload_image(self, path_to_file: str) -> None:
        with open(path_to_file, 'rb') as f:
            r = requests.request('post', constant.UPLOAD_URL, files={'imagedata': f}, headers={
                'Authorization': 'Bearer ' + self.__access_token})
            print(r)


gyazo_uploader = GyazoUploader(ConfigedParser())
