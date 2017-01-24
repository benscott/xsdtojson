import os
import simplejson as json
from lxml import etree
from collections import OrderedDict
from distutils.util import strtobool


from xsdtojson.lib import inflate_tag


class XSDParser:
    def __init__(self, xsd_file):
        path = os.path.abspath(xsd_file)
        # Check XSD file exists and raise error if not, rather than lxml error
        if not os.path.exists(xsd_file):
            raise IOError('XSD file %s does not exist' % xsd_file)

        self.doc = etree.parse(path)
        self.root = self.doc.getroot()
        self.namespaces = self.root.nsmap
        # Build all extensions - extended by the main elements
        self.type_extensions = self._get_type_extensions()

    def _get_type_extensions(self):
        """ Build a list of all type extensions which can be extended by the main class
        For example - http://www.w3schools.com/xml/el_complextype.asp
        """
        type_extensions = {}
        for complex_type in self.root.findall("xs:complexType", namespaces=self.namespaces):
            name = complex_type.attrib['name']
            type_extensions[name] = {
                'all': False,
                'sequence': False,
                'elements': []
            }
            for el in complex_type.iterdescendants():
                # FIXME: Ignore complex content, but it can be used to specify content restrictions
                if el.tag == inflate_tag('xs:complexContent', self.namespaces):
                    continue
                # Is this a sequence of elements (order is enforced)
                if el.tag == inflate_tag('xs:sequence', self.namespaces):
                    type_extensions[name]['sequence'] = True
                # Is this extending another group?
                if el.tag == inflate_tag('xs:extension', self.namespaces):
                    # Get name of groups this is extending
                    extension_base = el.attrib['base']
                    # Merge in the extension fields in
                    type_extensions[name]['elements'] += type_extensions[extension_base]['elements']
                if el.tag == inflate_tag('xs:element', self.namespaces):
                    # FIXME: What other attributes are required??
                    type_extensions[name]['elements'].append({
                        'name': el.attrib.get('name'),
                        'type': el.attrib.get('type')
                    })
        return type_extensions

    def json_schema(self):
        """
        Main entry point - convert the XSD file to
        :return:
        """
        schema = OrderedDict([
            ('$schema', 'http://json-schema.org/schema#'),
            ('properties', OrderedDict()),
            ('required', [])
        ])

        for element in self.root.findall("xs:element", namespaces=self.namespaces):
            element_name = element.attrib.get('name')
            element_type = element.attrib.get('type')
            nillable = element.attrib.get('nillable', None)
            # If we have a value for nillable, convert it to bool
            if nillable:
                nillable = strtobool(nillable)

            # If element has type, this isn't a complex type - it either uses a previously defined
            # extension, or is a simple type
            if element_type:
                try:
                    schema['properties'][element_name] = self.type_extensions[element_type]
                except KeyError:
                    schema['properties'][element_name] = {
                        'type': element_type
                    }
                    if not nillable:
                        schema['required'].append(element_name)
            else:
                # Elements can include complex types and multiple elements
                print(element)
                pass


        # for element in self.root.findall("xs:element", namespaces=self.namespaces):
        #     # el_type = element.attrib.get('type')
        #     # FIXME: if(el_type):
        #     #     schema.append()
        #
        #     print(element)

        return json.dumps(schema, sort_keys=False, indent=4)

        # print(els)

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


        # # elements = root.xpath('/element')

        # # print(elements)

        # # for el in root:
        # #     print(el)

        # # print(tree.getroot())
