try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

with open("README.md", 'r') as f:
        long_description = f.read()

config = {
        'description': 'TV Player',
        'author': 'Boban Ljubicic',
        'author_email': 'ljubicic.bobo@gmail.com',
        'version': '1.0',
        'install_requires': ['kivy==1.10.0', 'urllib3==1.22'],
        'packages': ['SimpleTV'],
        'name': 'SimpleTV'
}

setup(**config)
