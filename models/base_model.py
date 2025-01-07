#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model with optional attributes from kwargs"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at') and isinstance(
                        value, str
                    ):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.utcnow())
            self.updated_at = kwargs.get('updated_at', datetime.utcnow())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return f'[{cls}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates `updated_at` and saves instance to storage"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes this BaseModel instance from the storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        res = {
            key: (value.isoformat() if isinstance(value, datetime) else value)
            for key, value in self.__dict__.items()
            if key != '_sa_instance_state'
        }
        res['__class__'] = self.__class__.__name__
        return res
