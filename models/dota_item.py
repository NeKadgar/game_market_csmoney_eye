import datetime
from sqlalchemy.exc import IntegrityError
from extentions import db
from models.base_item import BaseItem


class DotaItem(BaseItem):
    __tablename__ = 'dota_item'

    history = db.relationship('DotaItemHistory', backref='item', lazy='dynamic')

    def __repr__(self):
        return f"{self.id}.{self.name}"

    @classmethod
    def get_or_create(cls, name: str, **kwargs):
        instance = cls.query.filter_by(name=name).one_or_none()
        if instance:
            return instance, False
        instance = cls(name=name)
        try:
            db.session.add(instance)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return cls.query.filter_by(name=name).one(), True


class DotaItemHistory(db.Model):
    """History price model"""
    __tablename__ = 'dota_item_history'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(precision=6, scale=2), nullable=False)
    default_price = db.Column(db.Numeric(precision=6, scale=2), nullable=False)
    slots = db.Column(db.JSON, default=None, nullable=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    item_id = db.Column(db.Integer, db.ForeignKey('dota_item.id'))

    def __repr__(self):
        return f"< {self.item} - {self.price} >"
