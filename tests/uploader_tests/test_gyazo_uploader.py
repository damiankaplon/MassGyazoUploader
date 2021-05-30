#!usr/bin/env/python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

import builtins
from unittest import TestCase
from uploader.gyazo_uploader import GyazoUploader
from uploader.configed_parser import ConfigedParser
from unittest.mock import patch


class TestGyazoUploader(TestCase):
    def setUp(self) -> None:
        pass
