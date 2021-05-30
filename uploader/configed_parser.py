#!/usr/bin/env python3.9

__all__ = ['ConfigedParser', 'ParserException']
__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

import argparse
import warnings
from argparse import ArgumentParser
from getpass import getpass


class ParserException(BaseException):
    pass


class ConfigedParser(ArgumentParser):
    """
    Class which object is going to be created/used just once. I thought its good idea, but seems to be kinda stupid.
    """
    def __init__(self):
        super().__init__(argument_default=argparse.SUPPRESS)
        self.add_argument("-u", help="Login. Required argument", default="None")
        self.add_argument("-p", help="Password", default="None")
        self.add_argument("-dir", help="path to directory. Required Argument", default="None")
        self.__args: dict = vars(self.parse_args())
        #self.pass_arg()

    def get_args(self) -> dict:
        return self.__args

    def check_for_user_arg(self) -> bool:
        """Checks if username is typed in and if it atleast seems to be a valid name"""
        arg_u: str = self.__args.get('u')
        if arg_u == 'None':
            return False
        else:
            return True

    def check_for_dir_arg(self) -> bool:
        """Checks if dir is typed in and if it atleast seems to be a valid name"""
        arg_d: str = self.__args.get('dir')
        if arg_d == 'None':
            return False
        elif arg_d.isascii():
            return True

    def pass_arg(self):
        arg_p: str = self.__args.get('p')
        if arg_p == "None":
            arg_p = getpass()
        else:
            print("Your password was typed in as argument in CLI. Everyone could see that!")
