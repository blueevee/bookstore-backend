from flask_marshmallow import Marshmallow
from marshmallow import INCLUDE, fields, validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema, auto_field

from .model import Masterpiece


ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class MasterpieceSchema(SQLAlchemyAutoSchema):

    id = fields.Int(required=False)
    title = fields.Str(required=True)
    company = fields.Str(required=True)
    company = fields.Str(required=False)
    image = fields.Str(required=False)
    authors = fields.Str(required=True)
    
    class Meta:
        model = Masterpiece
        # unknown = INCLUDE
        # include_relationships = True
        load_instance = True

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Não envie pelo amor de deus o ID')
