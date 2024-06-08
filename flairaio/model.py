""" Data classes for Flair API """
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class FlairData:
    """ Dataclass for Flair data. """

    users: dict[str, User]
    structures: dict[str, Structure]


@dataclass
class Users:
    """ Dataclass containing all Flair users """

    users: dict[str, User]


@dataclass
class User:
    """ Dataclass for Flair User """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    type: str = 'users'


@dataclass
class Structures:
    """ Dataclass containing all Flair Structures """

    structures: dict[str, Structure]


@dataclass
class Structure:
    """ Dataclass for Flair structure """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    rooms: dict[str, Room] | None = 'Not Fetched'
    pucks: dict[str, Puck] | None = 'Not Fetched'
    vents: dict[str, Vent] | None = 'Not Fetched'
    bridges: dict[str, Bridge] | None = 'Not Fetched'
    thermostats: dict[str, Thermostat] | None = 'Not Fetched'
    hvac_units: dict[str, HVACUnit] | None = 'Not Fetched'
    zones: dict[str, Zone] | None = 'Not Fetched'
    schedules: dict[str, Schedule] | None = "Not Fetched"
    type: str = 'structures'


@dataclass
class Rooms:
    """ Dataclass for Flair rooms """

    rooms: dict[str, Room]


@dataclass
class Room:
    """ Dataclass for Flair room """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    type: str = 'rooms'


@dataclass
class Pucks:
    """ Dataclass for Flair pucks """

    pucks: dict[str, Puck]


@dataclass
class Puck:
    """ Dataclass for Flair puck """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    current_reading: dict[str, Any] | None = 'Not Fetched'
    type: str = 'pucks'


@dataclass
class Vents:
    """ Dataclass for Flair vents """

    vents: dict[str, Vent]


@dataclass
class Vent:
    """ Dataclass for Flair vent """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    current_reading: dict[str, Any] | None = 'Not Fetched'
    type: str = 'vents'


@dataclass
class Bridges:
    """ Dataclass for Flair bridges """

    bridges: dict[str, Bridge]


@dataclass
class Bridge:
    """ Dataclass for Flair bridge """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    current_reading: dict[str, Any] | None = 'Not Fetched'
    type: str = 'bridges'


@dataclass
class Thermostats:
    """ Dataclass for thermostats """

    thermostats: dict[str, Thermostat]


@dataclass
class Thermostat:
    """ Dataclass for Thermostat """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    type: str = 'thermostats'


@dataclass
class HVACUnits:
    """ Dataclass for HVAC units """

    hvacs: dict[str, HVACUnit]


@dataclass
class HVACUnit:
    """ Dataclass for HVAC unit """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    type: str = 'hvac-units'


@dataclass
class Zones:
    """ Dataclass for Flair zones """

    zones: dict[str, Zone]


@dataclass
class Zone:
    """ Dataclass for Flair zone """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    type: str = 'zones'


@dataclass
class Schedule:
    """ Dataclass for Flair Structure schedule """

    id: str
    attributes: dict[str, Any]
    relationships: dict[str, Any]
    type: str = 'schedules'
