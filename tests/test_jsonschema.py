from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
from jsonschema import validate
from pathlib import Path
import jsonschema
import json
import os


class TestJSONSchema(object):

    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        cls.src_dir = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'src')

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""

    def test_valid_validation(self):
        """ Test validation via schema """
        with open(os.path.join(self.src_dir, 'basic.schema.json')) as schema_json:
            schema = json.load(schema_json)

        with open(os.path.join(self.src_dir, 'basic-valid.json')) as basic_json:
            basic_data = json.load(basic_json)

        validate(basic_data, schema)

    def test_invalid_validation(self):
        """ Test validation via schema """
        with open(os.path.join(self.src_dir, 'basic.schema.json')) as schema_json:
            schema = json.load(schema_json)

        with open(os.path.join(self.src_dir, 'basic-invalid.json')) as basic_json:
            basic_data = json.load(basic_json)

        # Check that this raises a validation error
        with assert_raises(jsonschema.exceptions.ValidationError):
            validate(basic_data, schema)
