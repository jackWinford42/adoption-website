from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import NumberRange, URL, AnyOf, Optional

valid_species = ['cat', 'dog', 'porcupine']

class AddPet(FlaskForm):
    """Form for adding pets"""

    name = StringField("Name")
    species = StringField("Species",
                        validators=[AnyOf(valid_species)])
    url = StringField("Photo Url",
                        validators=[URL(), Optional()])
    age = IntegerField("Age in Years",
                        validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")

class EditPet(FlaskForm):
    """edit certain information about a pet"""

    url = StringField("Photo Url",
                        validators=[URL(), Optional()])
    notes = StringField("Notes")
    available = BooleanField("Availability")