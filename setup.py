from pip.req import parse_requirements
from setuptools import setup

install_requirements = parse_requirements('./requirements.txt', session=False)
requirements = [str(ir.req) for ir in install_requirements]

setup(
    name='xsdtojson',
    version='0.1',
    description='Convert XSD to JSON Schema',
    author='Ben Scott',
    author_email='ben@benscott.co.uk',
    packages=['xsdtojson'],
    install_requires=requirements,
    entry_points={
        'console_scripts': ['xsdtojson=xsdtojson.cli:main'],
    }
)
