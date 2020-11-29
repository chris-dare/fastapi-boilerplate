"""
The :mod:`app.db.base_class` module implements base classes for DB models in the application
"""
from typing import Any
from neomodel import StructuredNode

class BaseStructuredNode(StructuredNode):
    id: Any
    __name__: str
