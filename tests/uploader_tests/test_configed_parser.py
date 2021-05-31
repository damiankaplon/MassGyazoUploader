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

    @patch.object(sys, 'argv', ['python'])
    def test_no_arguments(self) -> None:
        """Simulates situation when no arguments have been typed in CLI"""
        with patch.object(ConfigedParser, 'pass_arg', new=self.moc_get_pass):
            self.parser = ConfigedParser()
            self.assertEqual(self.parser.get_args(), {'u': 'None', 'p': 'None', 'dir': 'None'})

    @patch.object(sys, 'argv', ['python', '-u=damian'])
    def test_check_for_user_arg(self):
        """Simulates situation when user argument have been typed in CLI"""
        with patch.object(ConfigedParser, 'pass_arg', new=self.moc_get_pass):
            self.parser = ConfigedParser()
            self.assertEqual(self.parser.check_for_user_arg(), True)

    @patch.object(sys, 'argv', ['python', '-u=None'])
    def test_check_for_user_arg2(self):
        """Simulates situation when user argument have been not typed in CLI"""
        with patch.object(ConfigedParser, 'pass_arg', new=self.moc_get_pass):
            self.parser = ConfigedParser()
            self.assertEqual(self.parser.check_for_user_arg(), False)

    @patch.object(sys, 'argv', ['python'])
    def test_check_for_dir_arg(self):
        """Simulates situation when dir argument have been not typed in CLI"""
        with patch.object(ConfigedParser, 'pass_arg', new=self.moc_get_pass):
            self.parser = ConfigedParser()
            self.assertEqual(self.parser.check_for_dir_arg(), False)

    @patch.object(sys, 'argv', ['python', '-dir=C://'])
    def test_check_for_dir_arg2(self):
        """Simulates situation when dir argument have been typed in CLI"""
        with patch.object(ConfigedParser, 'pass_arg', new=self.moc_get_pass):
            self.parser = ConfigedParser()
            self.assertEqual(self.parser.check_for_dir_arg(), True)

    @patch.object(sys, 'argv', ['python', '-dir=C://', '-u=damian', '-p=pass'])
    def test_pass_arg(self):
        """Simulates situation when p argument have been typed in CLI"""
        with patch('builtins.print') as mock_print:
            ConfigedParser()
        mock_print.assert_called_with('Your password was typed in as argument in CLI. Everyone could see that!')

    def moc_get_pass(self):
        return


if "__main__" == __name__:
    unittest.main()
