#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '25/01/2017'.
"""
from xsdtojson.xsd_parser import XSDParser


def xsd_to_json_schema(xsd_src):
    """
    Helper function for instigating XSDParser and parsing file
    :param xsd_src: Path to XSD file / string
    :return:
    """
    xsd_parser = XSDParser(xsd_src)
    return xsd_parser.json_schema()
