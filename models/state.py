#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """Get all cities related"""
            c_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    c_list.append(city)
            return c_list
