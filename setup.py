from setuptools import setup, find_packages

import click_extensions


tests_require = [
    'flake8>=2.4.0',
    'pytest>=2.5.0',
]

install_requires = [
    'Click>=6.0',
]

setup(
    name='click-extensions',
    version=click_extensions.__version__,
    author='Naphat Sanguansin',
    author_email='naphat.krit@gmail.com',
    description='TigerHost Command-Line Client',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={'tests': tests_require},
    tests_require=tests_require,
    url='https://github.com/naphatkrit/click-extensions',
)
