"""Constant for FlairAIO"""

from .str_enum import StrEnum

TIMEOUT = 5 * 60

# Endpoint URLs
class Endpoint(StrEnum):
    """Flair API endpoints."""

    BASE_URL = 'https://api.flair.co'
    AUTH_URL = '/oauth2/token'
    BRIDGES_URL = '/api/bridges'
    HVACS_URL = '/api/hvac-units'
    PUCKS_URL = '/api/pucks'
    ROOMS_URL = '/api/rooms'
    STRUCTURES_URL = '/api/structures'
    THERMOSTATS_URL = '/api/thermostats'
    USERS_URL = '/api/users'
    VENTS_URL = '/api/vents'
    ZONES_URL = '/api/zones'


# Headers constants
class Header(StrEnum):
    """Flair client header constants."""

    CONTENT_ENCODED = 'application/x-www-form-urlencoded'
    CONTENT_JSON = 'application/json'
    ACCEPT = 'application/json'
    CLIENT_ID = 'client_id'
    CLIENT_SECRET = 'client_secret'
    SCOPES = 'pucks.view+pucks.edit+structures.view+structures.edit+thermostats.view+users.view+users.edit+vents.view+vents.edit'
    GRANT_CLIENT_CRED = 'client_credentials'


# Response error reason constants
class Reason(StrEnum):
    """Flair client response error reason constants."""

    CREATED = 'CREATED'
    FORBIDDEN = 'FORBIDDEN'
    INVALID_CLIENT = 'invalid_client'
    UNPROC_ENTITY = 'UNPROCESSABLE ENTITY'
