#!/usr/bin/env python3.9

__all__ = ['ConfigedParser']
__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

from argparse_prompt import PromptParser


class ConfigedParser(PromptParser):
    """
    Class which object is going to be created/used just once. I thought its good idea, but seems to be kinda stupid.
    Doesnt mae sens to create class just for one object
    """
    def __init__(self):
        super().__init__()
        self.add_argument("-u", help="Login")
        self.add_argument("-p", secure="True", help="Password")
        self.add_argument("dir", help="path to directory")
        self.__args: dict = vars(self.parse_args())

    def get_args(self) -> dict:
        return self.__args
