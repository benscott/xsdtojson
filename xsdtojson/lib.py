#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '25/01/2017'.
"""
from xsdtojson.xsd_parser import XSDParser


def xsd_to_json_schema(xsd_file_path):
    """
    Helper function for instigating XSDParser and parsing file
    :param xsd_file_path: Path to XSD file
    :return:
    """
    xsd_parser = XSDParser(xsd_file_path)
    return xsd_parser.json_schema()
