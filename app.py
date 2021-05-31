"""Adoption application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "thisIsSecret"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """display the homepage which is a list of pets in the adoption center"""

    pets = Pet.query.order_by(Pet.name).all()

    return render_template('home.html',
                    title="Pets",
                    pets=pets)

@app.route('/add', methods=["GET", "POST"])
def new_pet():
    """display a form for adding pets to the adoption center data
    and handle the form on submission"""

    form = AddPet()

    if form.validate_on_submit():

        pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.url.data or None,
            age = form.age.data,
            notes = form.notes.data,
            available = True
        )
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('add_pet.html',
                                title="Add a Pet",
                                form=form)

@app.route('/<pet_id>', methods=["GET", "POST"])
def display_and_edit_pet(pet_id):
    """display information about a pet and a form to edit that pet"""
    
    form = EditPet()

    pet = Pet.query.get_or_404(pet_id)

    if form.validate_on_submit():
        
        #if the url field is blank then use the default url
        pet.photo_url = form.url.data or "https://bit.ly/3y8O4Be"
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('display_and_edit.html',
                                title=pet.name,
                                form=form,
                                pet=pet)