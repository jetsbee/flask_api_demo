from marshmallow import (
    Schema,
    fields,
    validate,
    post_load,
)

from ..models.token import RevokedTokenModel


class TokenSchema(Schema):
    _id = fields.Str(validate=validate.Regexp(r'^[0-9A-Fa-f]{24}$'))
    jti = fields.Str(required=True)
    created_at = fields.DateTime()

    @post_load
    def make_object(self, data):
        if not data:
            return None
        return RevokedTokenModel(**data)
