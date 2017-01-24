import click
from pygments import highlight, lexers, formatters
from xsdtojson.xsd_parser import XSDParser


@click.command()
@click.argument('xsd_file')
def main(xsd_file):
    """Parse XSD file """
    xsd_parser = XSDParser(xsd_file)
    json_schema = xsd_parser.json_schema()
    # FIXME: This will not work if being piped
    print(highlight(json_schema, lexers.JsonLexer(), formatters.TerminalFormatter()))

if __name__ == '__main__':
    main()
