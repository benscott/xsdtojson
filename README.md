# XSD To JSON Schema

### Transforming XSD files into JSON Schema

Python script that converts XSD files into [JSON Schema](http://json-schema.org/).  

For example, transforming:
```
<?xml version="1.0" encoding="UTF-8" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:element name="example" type="xs:string" nillable="true" />
</xs:schema>
```
Into:
```
{
    "properties": {
        "example": {
            "type": "string"
        }
    },
    "required": [
        "example"
    ],
    "$schema": "http://json-schema.org/schema#"
}
```
### USAGE

#### CLI

Output JSON schema to stdout.
```
xsdtojson [PATH TO XSD FILE] --pretty
```
Output JSON schema to file
```
xsdtojson [PATH TO XSD FILE] > [PATH TO JSON OUTPUT FILE]
```

#### PYTHON
```
from xsdtojson import xsd_to_json_schema
json_schema = xsd_to_json_schema([PATH TO XSD FILE])
```

### TODO

* Convert XSD data types to JSON Schema types.  See generateRS for possible mappings.
* Add JSON-LD URI to schema - potential refs:
    * https://github.com/geraintluff/schema-org-gen
    * http://stackoverflow.com/questions/17768805/schema-org-ontology-as-json
    * https://gist.github.com/stain/7690362
    * http://json-schema.org/latest/json-schema-core.html#rfc.section.5.4
* Write tests. Ideally these will:
    * Build a JSON schema from XSD
    * Create & validate JSON-LD record
    * Use online JSON-LD=>RDF converter, and validated JSON_LD against original XSD.
* Convert more XSD sources:
    * http://musicontology.com/docs/getting-started.html
   