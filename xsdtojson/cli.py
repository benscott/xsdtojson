import click

from xsdtojson.xsd_parser import XSDParser


@click.command()
@click.argument('xsd_file')
def main(xsd_file):
    """Parse XSD file """
    xsd_parser = XSDParser(xsd_file)
    json_schema = xsd_parser.json_schema()
    print(json_schema)


if __name__ == '__main__':
    main()
