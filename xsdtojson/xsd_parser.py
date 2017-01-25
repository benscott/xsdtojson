import os
import simplejson as json
from lxml import etree
from collections import OrderedDict
from distutils.util import strtobool
from xsdtojson.lib import inflate_tag


class XSDParser:

    type_extensions = {}

    def __init__(self, xsd_file):
        path = os.path.abspath(xsd_file)
        # Check XSD file exists and raise error if not, rather than lxml error
        if not os.path.exists(xsd_file):
            raise IOError('XSD file %s does not exist' % xsd_file)
        self.doc = etree.parse(path)
        self.root = self.doc.getroot()
        self.namespaces = self.root.nsmap
        self.type_extensions = self._get_type_extensions()

    def _get_type_extensions(self):
        """ Build a list of all type extensions which can be extended by the main class
        For example - http://www.w3schools.com/xml/el_complextype.asp
        """
        type_extensions = {}
        for complex_type_element in self.root.findall("xs:complexType", namespaces=self.namespaces):
            name = complex_type_element.attrib['name']
            type_extensions[name] = self.parse_elements_recurse(complex_type_element)
        return type_extensions

    def parse_elements_recurse(self, root):
        """
        Recursively parse elements
        :param root:
        :return:
        """
        schema = OrderedDict()
        for element in root.getchildren():
            # Does this element have any element descendants?
            if element.findall(".//xs:element", namespaces=self.namespaces):
                child_schema = self.parse_elements_recurse(element)
                # Are there any actual properties within these child elements
                if 'properties' in child_schema:
                    # If we don't yet have properties, just use this.
                    # FIXME: This is probably what's breaking dwc?
                    if not any(schema):
                        schema = child_schema
                    else:
                        element_name = element.attrib.get('name', None)
                        # As per XSD spec maxOccurs defaults to 1
                        max_occurs = element.attrib.get('maxOccurs', 1)
                        # Can also be set to "unbounded" so need to handle casting to int
                        try:
                            max_occurs = int(max_occurs)
                        except ValueError:
                            pass
                        # FIXME: Need to loop back up for last parents - not sure this will work for nested
                        schema.setdefault('properties', OrderedDict())
                        schema['properties'][element_name] = child_schema
                        # If any of the child properties are required, then the whole set
                        # Becomes a requirement of the parent item
                        if 'required' in child_schema:
                            schema.setdefault('required', []).append(element_name)
                        # If maxOccurs is 1 or not set (defaults to 1), then the type is a dict
                        # If > 1 or unbound, this can be a list of dicts
                        # FIXME: Doesn't work for the root element
                        schema['properties'][element_name]['type'] = 'object' if max_occurs == 1 else 'array'
            else:
                element_type = element.attrib.get('type')
                element_name = element.attrib.get('name')
                # If there's no element name, skip it.  Without an identifier there's
                # very little that can be done with it - and seem to be annotations
                if not element_name:
                    continue
                # As per XSD spec, minOccurs defaults to 1, so unless
                # otherwise stated, all fields are required
                min_occurs = int(element.attrib.get('minOccurs', 1))
                nillable = strtobool(element.attrib.get('nillable')) if element.attrib.get('nillable') else False
                try:
                    self.type_extensions[element_type]
                    # schema['properties'][element_name] = self.type_extensions[element_type]
                    # print(schema)
                    pass
                except KeyError:
                    # Create properties dict if it doesn't already exist
                    schema.setdefault('properties', OrderedDict())
                    schema['properties'][element_name] = {
                        'type': element_type
                    }
                # If min occurs
                if min_occurs > 0 or nillable:
                    schema.setdefault('required', []).append(element_name)

        return schema

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

        schema = self.parse_elements_recurse(self.root)

        print('OUTPUT')
        print(schema)


        # for element in self.root.iterdescendants():
        #     if element.getchildren():
        #         pass
        #     else:
        #         element_type = element.attrib.get('type')
        #         element_name = element.attrib.get('name')
        #         print(element_type)
        #         print(element_name)


        # for element in self.root.findall("xs:element", namespaces=self.namespaces):
        #     element_name = element.attrib.get('name')
        #     element_type = element.attrib.get('type')
        #     nillable = element.attrib.get('nillable', None)
        #     # If we have a value for nillable, convert it to bool
        #     if nillable:
        #         nillable = strtobool(nillable)
        #
        #     # If element has type, this isn't a complex type - it either uses a previously defined
        #     # extension, or is a simple type
        #     if element_type:
        #         try:
        #             schema['properties'][element_name] = self.type_extensions[element_type]
        #         except KeyError:
        #             schema['properties'][element_name] = {
        #                 'type': element_type
        #             }
        #             if not nillable:
        #                 schema['required'].append(element_name)
        #     else:
        #         # Elements can include complex types and multiple elements
        #         print(element)
        #         pass


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
