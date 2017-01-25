# xsdtojson

### Convert XSD files to JSON Schema

Python script that converts XSD files to JSON Schema.

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
            "type": "xs:string"
        }
    },
    "required": [
        "example"
    ],
    "$schema": "http://json-schema.org/schema#"
}
```
### USAGE


### TODO

Not working with nested??

Can I run tests to build a JSON schema, validate a JSON-LD file against it, and then convert that back to RDF to validate against the original file?



Possible structure for mixing JSON-LD & Schema: https://github.com/geraintluff/schema-org-gen

http://stackoverflow.com/questions/17768805/schema-org-ontology-as-json

https://gist.github.com/stain/7690362

http://musicontology.com/docs/getting-started.html

https://groups.google.com/forum/#!topic/json-schema/d4XHU5jQKhI********

https://brandur.org/elegant-apis

https://github.com/interagent/prmd

https://www.haykranen.nl/2015/07/08/perfect-cms/