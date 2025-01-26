from app import app
from flask_sqlalchemy import SQLAlchemy
import os

# set up db
db_path = "sqlite:///" + os.path.join(os.path.dirname(__file__), 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# create models

class Team(db.Model):
    
    __tablename__ = 'teams'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text)
    abrv = db.Column(db.Text)
    common_name = db.Column(db.Text)
    place_name = db.Column(db.Text)
    logo_url = db.Column(db.Text)
    logo_url_dark = db.Column(db.Text)
    
    def __init__(self, id, full_name, abrv, common_name, place_name, logo_url, logo_url_dark):
        self.id = id
        self.full_name = full_name
        self.abrv = abrv
        self.common_name = common_name
        self.place_name = place_name
        self.logo_url = logo_url
        self.logo_url_dark = logo_url

    def __repr__(self):
        return f"Team: {self.full_name} - {self.abrv}"