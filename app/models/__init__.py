# Author: Chris Dare
# License:
from neomodel import config

from app.core.config import settings
from app.models.user import User

config.DATABASE_URL = settings.NEO4J_DATABASE_URI
