from Requirments import Images
from setuptools import setup

APP = ['Main_App.py']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=[*Images],
    options={'py2exe': OPTIONS},
    setup_requires=['py2exe']
)
