try:
    from setuptools import setup
execpt ImportError:
    from distutils.core import setup

config = {
    'description': 'Lexicon',
    'author': "Casey Spence",
    'url': "URL to get it at",
    'download_url': 'Where to download it',
    'author_email': 'orangobang@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'lexicon practice'
}

setup(**config)
