#!usr/bin/env/python3.9
from configed_parser import ConfigedParser
import constant
import requests
import os


class GyazoUploader:
    def __init__(self, parser: ConfigedParser):
        self.parser: ConfigedParser = parser
        self.__access_token: str = self.parser.get_args().get('p')
        self.__files_to_upload: list = []
        self.__save_credentials()
        self.__upload()

    def __save_credentials(self) -> None:
        username: str = self.parser.get_args().get('u')
        try:
            with open(constant.CONFIG_PATH, 'r+') as config_file:
                for line in config_file:
                    if username in line:
                        return None
                config_file.write("Login: {} \n".format(username))
                print("You login has been appended to config file")
        except FileNotFoundError:
            print("Couldn't localize '.gyazo' file in home catalog")

    def __upload(self) -> None:
        directory: str = self.parser.get_args().get('dir')
        dir_content = os.listdir(directory)
        for element in dir_content:
            if element.endswith(".jpg") or element.endswith(".png"):
                self.__files_to_upload.append(element)
        print(self.__files_to_upload)

        for file_path in self.__files_to_upload:
            self.__upload_image(file_path)

    def __upload_image(self, path_to_file: str) -> None:
        with open(path_to_file, 'rb') as f:
            r = requests.request('post', constant.UPLOAD_URL, files={'imagedata': f}, headers={
                'Authorization': 'Bearer ' + self.__access_token})
            print(r)


gyazo_uploader = GyazoUploader(ConfigedParser())
