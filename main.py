#!usr/bin/env/python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

from uploader.gyazo_uploader import GyazoUploader
from uploader.configed_parser import ConfigedParser


def main():
    GyazoUploader(ConfigedParser()).run()


if "__main__" == __name__:
    main()
