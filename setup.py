from distutils.core import setup

from setuptools import find_packages

setup(
    name='ping_in',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/Sarvar-K/django-ping-in',
    author='Sarvar-K',
    author_email='sarvar.kamilov1@gmail.com',
    description='Plug-in to ping current Django project',
    long_description_content_type="text/markdown",
    install_requires=[
        "Django>=4.0.0",
    ],
    setup_requires=['wheel'],
)
