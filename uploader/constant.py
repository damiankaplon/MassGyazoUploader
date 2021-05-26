#!usr/bin/env/python3.9
__all__ = ['CONFIG_PATH', 'UPLOAD_URL']
__version__ = '1.0'
__author__ = 'Damian Kaplon'
__email__ = 'kaplon.damian99@gmail.com'
__copyright___ = "Copyright (c) 2021 Damian Kaplon"

from pathlib import Path

CONFIG_PATH: str = "{}\\.gyazo".format(Path.home())
UPLOAD_URL: str = "https://upload.gyazo.com/api/upload"
