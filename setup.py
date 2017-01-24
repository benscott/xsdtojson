from setuptools import setup

setup(
    name='xsdtojson',
    version='0.1',
    description='Convert XSD to JSON Schema',
    author='Ben Scott',
    author_email='ben@benscott.co.uk',
    packages=['xsdtojson'],
    install_requires=[],
    entry_points={
        'console_scripts': ['xsdtojson=xsdtojson.cli:main'],
    }
)
