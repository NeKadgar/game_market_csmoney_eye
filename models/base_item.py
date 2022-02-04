from extentions import db


class BaseItem(db.Model):
    """Base steam service model of item"""
    __abstract__ = True

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
