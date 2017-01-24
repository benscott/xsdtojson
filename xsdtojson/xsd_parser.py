import os
from lxml import etree


class XSDParser:

    def __init__(self, xsd_file):
        path = os.path.abspath(xsd_file)
        # Check XSD file exists and raise error if not, rather than lxml error
        if not os.path.exists(xsd_file):
            raise IOError('XSD file %s does not exist' % xsd_file)

        self.doc = etree.parse(path)
        self.root = self.doc.getroot()
        self.namespaces = self.root.nsmap

    def _get_child_elements(self, element):
        return element.findall("xs:element", namespaces=self.namespaces)

    def json_schema(self):
        els = self._get_child_elements(self.root)
        print(els)

    # def json():
    #     for element in root.findall("xs:element", namespaces=namespaces):
    #         print(element.attrib['name'])
    #         print(element.attrib['type'])
    #         # print(element.items())
    #         # print(attr['name'])
    #         # Get attributes
    #         # print(element['name'])
    #         # Transform attributes to schema
    #         # http://www.dimuthu.org/blog/2008/08/18/xml-schema-nillabletrue-vs-minoccurs0/comment-page-1/
    #         print('---')
    # # for element in root.iterchildren('xs:element'):
    # #     print(element.tag)

    # # elements = root.xpath('/element')

    # # print(elements)

    # # for el in root:
    # #     print(el)

    # # print(tree.getroot())
