import xmlschema
schemaToCheck = xmlschema.XMLSchema('note-schema.xsd')
print(schemaToCheck.is_valid("note.xml"))