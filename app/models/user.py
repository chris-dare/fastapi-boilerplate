"""
The :mod:`app.models.user` module contains model classes to interface with the application databases.
Multiple user models for corresponding databases may be defined here
"""
# Author: Chris Dare
# License:

from neomodel import (
    BooleanProperty,
    EmailProperty,
    IntegerProperty,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)

from app.db.base_class import BaseStructuredNode


class User(BaseStructuredNode):
    id =  UniqueIdProperty()
    email = EmailProperty(unique_index=True)
    is_active = BooleanProperty(default=False)
    is_superuser = BooleanProperty(default=False)
    username = StringProperty(unique_index=True)
    first_name = StringProperty()
    last_name = StringProperty()
    hashed_password = StringProperty()
