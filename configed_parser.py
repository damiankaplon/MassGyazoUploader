#!/usr/bin/env python3.9
from argparse_prompt import PromptParser


class ConfigedParser(PromptParser):
    def __init__(self):
        super().__init__()
        self.add_argument("-u", help="Login")
        self.add_argument("-p", secure="True", help="Password")
        self.add_argument("dir", help="path to directory")
        self.__args: dict = vars(self.parse_args())

    def get_args(self) -> dict:
        return self.__args
