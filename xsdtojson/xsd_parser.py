#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '25/01/2017'.
"""
import simplejson as json
from lxml import etree
from collections import OrderedDict
from distutils.util import strtobool


class XSDParser:

    type_extensions = {}

    type_mappings = {}

    def __init__(self, xsd_src):

        try:
            # Try and read src as XML (will work for requests.content (string)
            self.root = etree.XML(xsd_src)
        except etree.XMLSyntaxError:
            # Or parse the object (will work for files)
            doc = etree.parse(xsd_src)
            self.root = doc.getroot()

        self.namespaces = self.root.nsmap
        self.build_type_extensions()

    def build_type_extensions(self):
        """ Build a list of all type extensions which can be extended by the main class
        For example - http://www.w3schools.com/xml/el_complextype.asp
        """
        for complex_type_element in self.root.findall("xs:complexType", namespaces=self.namespaces):
            name = complex_type_element.attrib['name']
            schema = {}
            self.parse_element_recurse(complex_type_element, schema)
            print(schema)
            schema = self.flatten_schema(schema)

            self.type_extensions[name] = schema

    def parse_element_recurse(self, element, schema):
        """
        Recursively parse elements
        :param element:
        :param schema:
        :return:
        """
        element_name = element.attrib.get('name')
        element_type = element.attrib.get('type')
        element_base = element.attrib.get('base')
        # As per XSD spec, minOccurs defaults to 1, so unless
        # otherwise stated, all fields are required
        min_occurs = int(element.attrib.get('minOccurs', 1))
        nillable = strtobool(element.attrib.get('nillable')) if element.attrib.get('nillable') else False

        # If element has an extension base, set properties to those of the extension
        if element_base:
            schema.update(self.type_extensions[element_base])
        # If this element has a name, add it to the schema tree
        elif element_name:
            # Create properties dict if it doesn't already exist
            schema.setdefault('properties', OrderedDict())
            # If this element has a type, it needs to be an item in the schema
            if element_type:
                try:
                    schema['properties'][element_name] = self.type_extensions[element_type]
                except KeyError:
                    schema['properties'][element_name] = {
                        'type': self.xsd_to_json_schema_type(element_type)
                    }
                if min_occurs > 0 or nillable:
                    schema.setdefault('required', []).append(element_name)
            # If there's no element type, use it to build the schema tree
            else:
                # If min occurs or nillable is set, then make this element required
                if min_occurs > 0 or nillable:
                    schema.setdefault('required', []).append(element_name)
                schema['properties'][element_name] = OrderedDict()
                # Update schema pointer to use the nested element
                # This allows us to build the tree
                schema = schema['properties'][element_name]

        # Does this element have any element descendants?
        # If does, recursively call function
        if element.findall(".//xs:element", namespaces=self.namespaces):
            for child_element in element.getchildren():
                self.parse_element_recurse(child_element, schema)

    @staticmethod
    def flatten_schema(schema):
        """
        If the top level properties dict consists of just one item, and has
        lots of child properties, flatten property dict
        TODO: This is to keep the schema the same as other plugins - is it needed?
        :param schema:
        :return:
        """
        if len(schema['properties']) == 1:
            first_property = next(iter(schema['properties']))
            # If the sole top level item has child properties, then flatten
            # If there's no child properties, do no flatten
            if 'properties' in schema['properties'][first_property]:
                schema = schema['properties'][first_property]
        return schema

    def json_schema(self):
        """
        Main entry point - convert the XSD file to
        :return:
        """
        schema = OrderedDict()
        # Starting point: all elements in the root of the document
        # This allows us to exclude complexType used as named types (e.g. tests/person.xsd)
        for element in self.root.findall("xs:element", namespaces=self.namespaces):
            self.parse_element_recurse(element, schema)

        # Flatten the schema - so if there's just one element at the root, this is removed
        schema = self.flatten_schema(schema)
        # Set schema
        schema['schema'] = 'http://json-schema.org/schema#'
        schema['type'] = 'object'
        return json.dumps(schema, sort_keys=False, indent=4)

    def xsd_to_json_schema_type(self, element_type):
        try:
            return self.type_mappings[element_type]
        except KeyError:
            return 'string'
