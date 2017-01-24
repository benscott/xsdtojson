# ./DWC.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8550a2f442f33189c46385bf081b232adcc0a226
# Generated 2017-01-23 21:09:26.873129 by PyXB version 1.2.5 using Python 3.5.0.final.0
# Namespace http://rs.tdwg.org/dwc/dwcore/

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:38a6b974-e1b0-11e6-a074-6003088b4170')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _dwe as _ImportedBinding__dwe

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://rs.tdwg.org/dwc/dwcore/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://rs.tdwg.org/dwc/dwcore/}positiveDouble
class positiveDouble (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positiveDouble')
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 23, 1)
    _Documentation = None
positiveDouble._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value=pyxb.binding.datatypes._fp(0.0), value_datatype=pyxb.binding.datatypes.double)
positiveDouble._InitializeFacetMap(positiveDouble._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'positiveDouble', positiveDouble)
_module_typeBindings.positiveDouble = positiveDouble

# Atomic simple type: {http://rs.tdwg.org/dwc/dwcore/}dayOfYearDataType
class dayOfYearDataType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dayOfYearDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 29, 1)
    _Documentation = None
dayOfYearDataType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.integer(1), value_datatype=dayOfYearDataType)
dayOfYearDataType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value=pyxb.binding.datatypes.integer(366), value_datatype=dayOfYearDataType)
dayOfYearDataType._InitializeFacetMap(dayOfYearDataType._CF_minInclusive,
   dayOfYearDataType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'dayOfYearDataType', dayOfYearDataType)
_module_typeBindings.dayOfYearDataType = dayOfYearDataType

# Atomic simple type: {http://rs.tdwg.org/dwc/dwcore/}decimalLatitudeDataType
class decimalLatitudeDataType (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'decimalLatitudeDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 36, 1)
    _Documentation = None
decimalLatitudeDataType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.double(-90.0), value_datatype=decimalLatitudeDataType)
decimalLatitudeDataType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value=pyxb.binding.datatypes.double(90.0), value_datatype=decimalLatitudeDataType)
decimalLatitudeDataType._InitializeFacetMap(decimalLatitudeDataType._CF_minInclusive,
   decimalLatitudeDataType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'decimalLatitudeDataType', decimalLatitudeDataType)
_module_typeBindings.decimalLatitudeDataType = decimalLatitudeDataType

# Atomic simple type: {http://rs.tdwg.org/dwc/dwcore/}decimalLongitudeDataType
class decimalLongitudeDataType (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'decimalLongitudeDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 43, 1)
    _Documentation = None
decimalLongitudeDataType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.double(-180.0), value_datatype=decimalLongitudeDataType)
decimalLongitudeDataType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value=pyxb.binding.datatypes.double(180.0), value_datatype=decimalLongitudeDataType)
decimalLongitudeDataType._InitializeFacetMap(decimalLongitudeDataType._CF_minInclusive,
   decimalLongitudeDataType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'decimalLongitudeDataType', decimalLongitudeDataType)
_module_typeBindings.decimalLongitudeDataType = decimalLongitudeDataType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 52, 5)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.double(0.0), value_datatype=STD_ANON)
STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value=pyxb.binding.datatypes.double(0.0), value_datatype=STD_ANON)
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive,
   STD_ANON._CF_maxInclusive)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 58, 5)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value=pyxb.binding.datatypes.double(1.0), value_datatype=STD_ANON_)
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 63, 5)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.undefined = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='undefined', tag='undefined')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: {http://rs.tdwg.org/dwc/dwcore/}DateTimeISO
class DateTimeISO (pyxb.binding.datatypes.string):

    """
              The date and time expressed in a way conforming to a subset of ISO 8601. Meant to be exactly the same as DateTimeISO defined in ABCD.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateTimeISO')
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 71, 8)
    _Documentation = '\n              The date and time expressed in a way conforming to a subset of ISO 8601. Meant to be exactly the same as DateTimeISO defined in ABCD.\n            '
DateTimeISO._CF_pattern = pyxb.binding.facets.CF_pattern()
DateTimeISO._CF_pattern.addPattern(pattern='\\d\\d\\d\\d(\\-(0[1-9]|1[012])(\\-((0[1-9])|1\\d|2\\d|3[01])(T(0\\d|1\\d|2[0-3])(:[0-5]\\d){0,2})?)?)?|\\-\\-(0[1-9]|1[012])(\\-(0[1-9]|1\\d|2\\d|3[01]))?|\\-\\-\\-(0[1-9]|1\\d|2\\d|3[01])')
DateTimeISO._InitializeFacetMap(DateTimeISO._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DateTimeISO', DateTimeISO)
_module_typeBindings.DateTimeISO = DateTimeISO

# Union simple type: {http://rs.tdwg.org/dwc/dwcore/}spatialFitDataType
# superclasses pyxb.binding.datatypes.anySimpleType
class spatialFitDataType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON, STD_ANON_, STD_ANON_2."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'spatialFitDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://rs.tdwg.org/dwc/tdwg_basetypes.xsd', 50, 1)
    _Documentation = None

    _MemberTypes = ( STD_ANON, STD_ANON_, STD_ANON_2, )
spatialFitDataType._CF_pattern = pyxb.binding.facets.CF_pattern()
spatialFitDataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=spatialFitDataType)
spatialFitDataType.undefined = 'undefined'        # originally STD_ANON_2.undefined
spatialFitDataType._InitializeFacetMap(spatialFitDataType._CF_pattern,
   spatialFitDataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'spatialFitDataType', spatialFitDataType)
_module_typeBindings.spatialFitDataType = spatialFitDataType

GlobalUniqueIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GlobalUniqueIdentifier'), pyxb.binding.datatypes.string, documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 58, 1))
Namespace.addCategoryObject('elementBinding', GlobalUniqueIdentifier.name().localName(), GlobalUniqueIdentifier)

DateLastModified = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DateLastModified'), pyxb.binding.datatypes.dateTime, documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 66, 1))
Namespace.addCategoryObject('elementBinding', DateLastModified.name().localName(), DateLastModified)

BasisOfRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BasisOfRecord'), pyxb.binding.datatypes.string, documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 74, 1))
Namespace.addCategoryObject('elementBinding', BasisOfRecord.name().localName(), BasisOfRecord)

InstitutionCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstitutionCode'), pyxb.binding.datatypes.string, documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 81, 1))
Namespace.addCategoryObject('elementBinding', InstitutionCode.name().localName(), InstitutionCode)

CollectionCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionCode'), pyxb.binding.datatypes.string, documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 89, 1))
Namespace.addCategoryObject('elementBinding', CollectionCode.name().localName(), CollectionCode)

CatalogNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CatalogNumber'), pyxb.binding.datatypes.string, documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 97, 1))
Namespace.addCategoryObject('elementBinding', CatalogNumber.name().localName(), CatalogNumber)

InformationWithheld = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InformationWithheld'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 104, 1))
Namespace.addCategoryObject('elementBinding', InformationWithheld.name().localName(), InformationWithheld)

Remarks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Remarks'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 112, 1))
Namespace.addCategoryObject('elementBinding', Remarks.name().localName(), Remarks)

ScientificName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScientificName'), pyxb.binding.datatypes.string, documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 118, 1))
Namespace.addCategoryObject('elementBinding', ScientificName.name().localName(), ScientificName)

HigherTaxon = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HigherTaxon'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 126, 1))
Namespace.addCategoryObject('elementBinding', HigherTaxon.name().localName(), HigherTaxon)

Kingdom = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Kingdom'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 133, 1))
Namespace.addCategoryObject('elementBinding', Kingdom.name().localName(), Kingdom)

Phylum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Phylum'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 139, 1))
Namespace.addCategoryObject('elementBinding', Phylum.name().localName(), Phylum)

Class = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 145, 1))
Namespace.addCategoryObject('elementBinding', Class.name().localName(), Class)

Order = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Order'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 151, 1))
Namespace.addCategoryObject('elementBinding', Order.name().localName(), Order)

Family = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Family'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 157, 1))
Namespace.addCategoryObject('elementBinding', Family.name().localName(), Family)

Genus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Genus'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 163, 1))
Namespace.addCategoryObject('elementBinding', Genus.name().localName(), Genus)

SpecificEpithet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpecificEpithet'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 169, 1))
Namespace.addCategoryObject('elementBinding', SpecificEpithet.name().localName(), SpecificEpithet)

InfraspecificRank = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InfraspecificRank'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 177, 1))
Namespace.addCategoryObject('elementBinding', InfraspecificRank.name().localName(), InfraspecificRank)

InfraspecificEpithet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InfraspecificEpithet'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 185, 1))
Namespace.addCategoryObject('elementBinding', InfraspecificEpithet.name().localName(), InfraspecificEpithet)

AuthorYearOfScientificName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AuthorYearOfScientificName'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 193, 1))
Namespace.addCategoryObject('elementBinding', AuthorYearOfScientificName.name().localName(), AuthorYearOfScientificName)

NomenclaturalCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NomenclaturalCode'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 201, 1))
Namespace.addCategoryObject('elementBinding', NomenclaturalCode.name().localName(), NomenclaturalCode)

IdentificationQualifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentificationQualifier'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 209, 1))
Namespace.addCategoryObject('elementBinding', IdentificationQualifier.name().localName(), IdentificationQualifier)

HigherGeography = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HigherGeography'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 217, 1))
Namespace.addCategoryObject('elementBinding', HigherGeography.name().localName(), HigherGeography)

Continent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Continent'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 225, 1))
Namespace.addCategoryObject('elementBinding', Continent.name().localName(), Continent)

WaterBody = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WaterBody'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 232, 1))
Namespace.addCategoryObject('elementBinding', WaterBody.name().localName(), WaterBody)

IslandGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IslandGroup'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 239, 1))
Namespace.addCategoryObject('elementBinding', IslandGroup.name().localName(), IslandGroup)

Island = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Island'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 246, 1))
Namespace.addCategoryObject('elementBinding', Island.name().localName(), Island)

Country = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Country'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 252, 1))
Namespace.addCategoryObject('elementBinding', Country.name().localName(), Country)

StateProvince = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StateProvince'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 258, 1))
Namespace.addCategoryObject('elementBinding', StateProvince.name().localName(), StateProvince)

County = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'County'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 265, 1))
Namespace.addCategoryObject('elementBinding', County.name().localName(), County)

Locality = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Locality'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 271, 1))
Namespace.addCategoryObject('elementBinding', Locality.name().localName(), Locality)

MinimumElevationInMeters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinimumElevationInMeters'), pyxb.binding.datatypes.double, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 277, 1))
Namespace.addCategoryObject('elementBinding', MinimumElevationInMeters.name().localName(), MinimumElevationInMeters)

MaximumElevationInMeters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaximumElevationInMeters'), pyxb.binding.datatypes.double, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 285, 1))
Namespace.addCategoryObject('elementBinding', MaximumElevationInMeters.name().localName(), MaximumElevationInMeters)

MinimumDepthInMeters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinimumDepthInMeters'), pyxb.binding.datatypes.double, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 293, 1))
Namespace.addCategoryObject('elementBinding', MinimumDepthInMeters.name().localName(), MinimumDepthInMeters)

MaximumDepthInMeters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaximumDepthInMeters'), pyxb.binding.datatypes.double, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 301, 1))
Namespace.addCategoryObject('elementBinding', MaximumDepthInMeters.name().localName(), MaximumDepthInMeters)

CollectingMethod = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectingMethod'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 309, 1))
Namespace.addCategoryObject('elementBinding', CollectingMethod.name().localName(), CollectingMethod)

ValidDistributionFlag = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValidDistributionFlag'), pyxb.binding.datatypes.boolean, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 317, 1))
Namespace.addCategoryObject('elementBinding', ValidDistributionFlag.name().localName(), ValidDistributionFlag)

Collector = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Collector'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 348, 1))
Namespace.addCategoryObject('elementBinding', Collector.name().localName(), Collector)

Sex = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sex'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 355, 1))
Namespace.addCategoryObject('elementBinding', Sex.name().localName(), Sex)

LifeStage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LifeStage'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 361, 1))
Namespace.addCategoryObject('elementBinding', LifeStage.name().localName(), LifeStage)

Attributes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Attributes'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 368, 1))
Namespace.addCategoryObject('elementBinding', Attributes.name().localName(), Attributes)

ImageURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImageURL'), pyxb.binding.datatypes.anyURI, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 375, 1))
Namespace.addCategoryObject('elementBinding', ImageURL.name().localName(), ImageURL)

RelatedInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RelatedInformation'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 381, 1))
Namespace.addCategoryObject('elementBinding', RelatedInformation.name().localName(), RelatedInformation)

EarliestDateCollected = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EarliestDateCollected'), DateTimeISO, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 325, 1))
Namespace.addCategoryObject('elementBinding', EarliestDateCollected.name().localName(), EarliestDateCollected)

LatestDateCollected = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LatestDateCollected'), DateTimeISO, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 333, 1))
Namespace.addCategoryObject('elementBinding', LatestDateCollected.name().localName(), LatestDateCollected)

DayOfYear = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DayOfYear'), dayOfYearDataType, nillable=pyxb.binding.datatypes.boolean(1), documentation='', location=pyxb.utils.utility.Location('/Users/bens3/Projects/Sparkd/lodb.io/xsdtojson/tdwg_dw_core.xsd', 341, 1))
Namespace.addCategoryObject('elementBinding', DayOfYear.name().localName(), DayOfYear)

GlobalUniqueIdentifier._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

DateLastModified._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

BasisOfRecord._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

InstitutionCode._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

CollectionCode._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

CatalogNumber._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

InformationWithheld._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Remarks._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

ScientificName._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

HigherTaxon._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Kingdom._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Phylum._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Class._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Order._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Family._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Genus._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

SpecificEpithet._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

InfraspecificRank._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

InfraspecificEpithet._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

AuthorYearOfScientificName._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

NomenclaturalCode._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

IdentificationQualifier._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

HigherGeography._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Continent._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

WaterBody._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

IslandGroup._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Island._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Country._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

StateProvince._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

County._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Locality._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

MinimumElevationInMeters._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

MaximumElevationInMeters._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

MinimumDepthInMeters._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

MaximumDepthInMeters._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

CollectingMethod._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

ValidDistributionFlag._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Collector._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Sex._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

LifeStage._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

Attributes._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

ImageURL._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

RelatedInformation._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

EarliestDateCollected._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

LatestDateCollected._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)

DayOfYear._setSubstitutionGroup(_ImportedBinding__dwe.dwElement)
