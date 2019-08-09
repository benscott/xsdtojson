import click
from pygments import highlight, lexers, formatters
from xsdtojson import xsd_to_json_schema


@click.command()
@click.argument('xsd_file', type=click.Path(exists=True))
@click.option('--pretty', '-p', is_flag=True)
def main(xsd_file, pretty):
    """ CLI interface for parsing XSD file """
    json_schema = xsd_to_json_schema(xsd_file)
    if pretty:
        json_schema = highlight(json_schema, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(json_schema)

if __name__ == '__main__':
    main()
