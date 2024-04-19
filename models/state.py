#!/usr/bin/python3
'''
This is the 'state' module.
'''
from models import *
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import *
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    '''This is the 'State' class'''
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""
        cities = ""

        @property
        def cities(self):
            cities = models.storage.all("City").values()
            result = [city_list for city in cities if city.state_id == self.id]
            return (result)

    def __init__(self, *args, **kwargs):
        '''This is the initialization method'''
        super(State, self).__init__(*args, **kwargs)
