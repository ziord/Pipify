from setuptools import setup
import os

def get_version():
    v = ''
    fp = os.path.join(os.getcwd(), "pipify", '__init__.py')
    with open(fp) as file:
        for line in file:
            if line.startswith('__version__'):
                v = line.split('__version__=')[-1].strip()
    return v

VERSION = get_version()

setup(
    name="pipify",
    version=VERSION,
    description="simple utility tool to generate requirements.txt file for Python projects",
    author="ziord"
)