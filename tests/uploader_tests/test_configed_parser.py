#!usr/bin/env/python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

import sys
import unittest
from unittest.mock import patch

from uploader.configed_parser import *
from unittest import TestCase


class TestConfigParser(TestCase):
    """Every test while testing uses method 'get_args' from class ConfigedParser, so there is no need
    to test this method in separated test"""
    def setUp(self) -> None:
        pass

    def test_no_arguments(self) -> None:
        """Simulates situation when no arguments have been typed in"""
        self.parser = ConfigedParser()
        self.assertEqual(self.parser.get_args(), {'u': 'None', 'p': 'None', 'dir': 'None'})

    def test_check_for_user_arg(self):
        sys.argv.append('-u=damian')
        self.parser = ConfigedParser()
        self.assertEqual(self.parser.check_for_user_arg(), True)

    def test_check_for_user_arg2(self):
        sys.argv.clear()
        sys.argv.append('-u=None')
        self.parser = ConfigedParser()
        self.assertEqual(self.parser.check_for_user_arg(), False)

    def test_check_for_dir_arg(self):
        self.parser = ConfigedParser()
        self.assertEqual(self.parser.check_for_dir_arg(), False)

    @patch('builtins.input', side_effect=['pass', 'pass', 'pass'])
    def test_check_for_dir_arg2(self, mock_input):
        sys.argv.append('-dir=C://')
        self.parser = ConfigedParser()
        self.assertEqual(self.parser.check_for_dir_arg(), True)


if "__main__" == __name__:
    unittest.main()
