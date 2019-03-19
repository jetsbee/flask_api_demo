from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
)

from ..models.user import UserModel


class UserSchema(Schema):
    _id = fields.Str(validate=validate.Regexp(r'^[0-9A-Fa-f]{24}$'))
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    access = fields.Int(validate=validate.Range(0, 2))
    created_at = fields.DateTime()

    @post_load
    def make_object(self, data):
        if not data:
            return None
        return UserModel(**data)
