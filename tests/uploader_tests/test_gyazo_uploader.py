#!usr/bin/env/python3.9

__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

import builtins
import sys
import unittest
from unittest import TestCase
from uploader.gyazo_uploader import GyazoUploader
from uploader.configed_parser import ConfigedParser
from unittest.mock import patch


class TestGyazoUploader(TestCase):
    def setUp(self) -> None:
        pass

    @patch.object(sys, 'argv', ['python'])
    def test_run(self):
        """Simulates situation when user typed nim directory which doesnt exists"""
        with patch.object(ConfigedParser, 'pass_arg', new=self.mock_method):
            with patch.object(GyazoUploader, 'valid_credentials', new=self.mock_method2):
                with patch.object(GyazoUploader, 'set_required_args', new=self.mock_method):
                    with patch('builtins.print') as mock_print:
                        uploader = GyazoUploader(ConfigedParser())
                        uploader.run('damian', 'notadirectory')
        mock_print.assert_called_with("Indicated directory can't be find!")

    def mock_method(self):
        return

    def mock_method2(self, arg):
        return


if "__main__" == __name__:
    unittest.main()
