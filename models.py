"""Models for adopt app."""
DEFAULT_IMAGE = "https://www.fortbendcountytx.gov/sites/default/files/media/2021-11/636776284196770000.jpg"

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
        )
    name = db.Column(
        db.Text,
        nullable=False
        )
    species = db.Column(
        db.Text,
        nullable=False,
     )
    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMAGE
    )
    age = db.Column(
        db.Text,
        nullable=False
    )
    notes = db.Column(
        db.Text,
        nullable=True
    )
    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

