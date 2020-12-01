#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '25/01/2017'.
"""
from .xsd_parser import XSDParser


def xsd_to_json_schema(xsd_src, code_mirror_format=False):
    """
    Helper function for instigating XSDParser and parsing file
    :param xsd_src: Path to XSD file / string
    :param code_mirror_format: Either using codemirror json format or not
    :return:
    """
    xsd_parser = XSDParser(xsd_src)
    return xsd_parser.json_schema(code_mirror_format=code_mirror_format)
