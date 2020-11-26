"""
The :mod:`app.schemas.token` module implements schema classes for tokens in the application.
"""

from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
