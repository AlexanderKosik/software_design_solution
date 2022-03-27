import json
import jsonschema

class JSONValidator:
    def __init__(self, schema_file):
        with open(schema_file) as f:
            self.schema = json.loads(f.read())
        

    def validate(self, book):
        """
        Raises a ValidationError on failure
        """
        payload = json.loads(book._json)
        jsonschema.validate(payload, self.schema)
    
