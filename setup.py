from distutils.core import setup

setup(
    name='PyDisdrometer',
    version='0.1.0',
    author='Joseph C. Hardin',
    author_email='josephhardinee@gmail.com',
    packages=['pydisdrometer'],
    url='http://pypi.python.org/pypi/PyDisdrometer/',
    licenese='LICENSE.txt',
    description='Pyton Disdrometer Processing',
    long_description=open('README.txt').read(),
    install_requires=[
        "pytmatrix >=0.2.0"
    ],
)
