from marshmallow import Schema, fields, validate

class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.String(validate=validate.Length(max=255), required=True)
    last_name = fields.String(validate=validate.Length(max=255), required=True)

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(validate=validate.Length(max=255), required=True)
    author_id = fields.Int(required=True)
