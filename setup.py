import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    package_dir = {'': 'OneTimePadEncryption'},
    name = "One_Time_Pad_Encryption_Utility",
    version = "1.0.0",
    author = "Marc Santiago",
    author_email = "marcanthonysanti@gmail.com",
    url = 'https://github.com/marcsantiago/one-time-pad-encryption',
    download_url = 'hhttps://github.com/marcsantiago/one-time-pad-encryption/tarball/0.1',
    long_description=read('README.txt'),
)