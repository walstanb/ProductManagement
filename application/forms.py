from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import *

class ProductForm(FlaskForm):
    product_id=StringField('product_id')
    submit=SubmitField('Submit')

class LocationForm(FlaskForm):
    location_id=StringField('location_id')
    submit=SubmitField('Submit')

class ProductMovementForm(FlaskForm):
    movement_id = StringField('movement_id')
    timestamp = StringField('timestamp')
    from_location = StringField('from_location')
    to_location = StringField('to_location')
    product_id = StringField('product_id')
    qty = StringField('qty')
    submit=SubmitField('Submit')