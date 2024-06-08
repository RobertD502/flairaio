"""Python client for Flair OAuth2 API."""
from __future__ import annotations

import asyncio
from datetime import datetime, timedelta
from typing import Any

from aiohttp import ClientResponse, ClientSession
from aiohttp.client_exceptions import ContentTypeError

from flairaio.constants import (
    Endpoint,
    Header,
    Reason,
    TIMEOUT,
)
from flairaio.exceptions import FlairError, FlairAuthError
from flairaio.model import (Bridge, Bridges, FlairData, HVACUnit, HVACUnits, Puck, Pucks, Room,
                            Rooms, Schedule, Structure, Structures, Thermostat,
                            Thermostats, User, Users, Vent, Vents, Zone, Zones,)


class FlairClient:
    """Flair Client."""

    def __init__(
            self, client_id: str, client_secret: str,
            session: ClientSession | None = None,
            timeout: int = TIMEOUT
    ) -> None:
        """
        client_id: OAuth 2.0 client_id provided by Flair
        client_secret: OAuth 2.0 client_secret provided by Flair
        session: aiohttp.ClientSession or None to create a new session
        """
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self._session = session if session else ClientSession()
        self.token: str | None = None
        self.token_expiration: datetime | None = None
        self.current_dt: datetime | None = None
        self.timeout: int = timeout

    async def get_token(self) -> None:
        """Get OAuth2 token using client credentials.

        OAuth 2.0 credentials are sent to Flair's servers in order to obtain a token
        as well as the expiration date and time.
        """

        headers = {
            "content-type": Header.CONTENT_ENCODED
        }

        data = {
            Header.CLIENT_ID: self.client_id,
            Header.CLIENT_SECRET: self.client_secret,
            "scope": Header.SCOPES,
            "grant_type": Header.GRANT_CLIENT_CRED
        }

        response = await self._post(Endpoint.AUTH_URL, headers, data)
        self.token = response['access_token']
        self.token_expiration = datetime.now() + timedelta(seconds=response['expires_in'])

    async def check_token(self) -> None:
        """Check to see if there is a valid token or if token is about to expire.

        If there is no token, a new token is obtained. In addition,
        if the current token is about to expire within 60 minutes
        or has already expired, a new token is obtained.
        """

        self.current_dt = datetime.now()
        if (self.token or self.token_expiration) is None:
            await self.get_token()
        elif (self.token_expiration-self.current_dt).total_seconds() < 3600:
            await self.get_token()
        else:
            return None

    async def get_users(self) -> Users:
        """Get all users' information."""

        fetched_users = await self._get(Endpoint.USERS_URL)
        users: dict[str, User] = {}
        if fetched_users['data']:
            for user in fetched_users['data']:
                users[user['id']] = User(
                    id=user['id'],
                    attributes=user['attributes'],
                    relationships=user['relationships'],
                )
        return Users(users=users)

    async def get_user(self, user_id: str) -> User:
        """Get a single user."""

        url = f'{Endpoint.USERS_URL}/{user_id}'
        user = await self._get(url)
        return User(
            id=user['data']['id'],
            attributes=user['data']['attributes'],
            relationships=user['data']['relationships'],
        )

    async def get_structures(self) -> Structures:
        """Get all structures."""

        fetched_structures = await self._get(Endpoint.STRUCTURES_URL)
        structures: dict[str, Structure] = {}

        if fetched_structures['data']:
            for structure in fetched_structures['data']:
                if structure['attributes'].get('setup-complete'):
                    structures[structure['id']] = Structure(
                        id=structure['id'],
                        attributes=structure['attributes'],
                        relationships=structure['relationships'],
                    )
        return Structures(structures=structures)

    async def get_structure(self, structure_id: str) -> Structure:
        """Get a single structure."""

        url = f'{Endpoint.STRUCTURES_URL}/{structure_id}'
        structure = await self._get(url)
        return Structure(
            id=structure['data']['id'],
            attributes=structure['data']['attributes'],
            relationships=structure['data']['relationships'],
        )

    async def get_rooms(self) -> Rooms:
        """Get all rooms."""

        fetched_rooms = await self._get(Endpoint.ROOMS_URL)
        rooms: dict[str, Room] = {}

        if fetched_rooms['data']:
            for room in fetched_rooms['data']:
                rooms[room['id']] = Room(
                        id=room['id'],
                        attributes=room['attributes'],
                        relationships=room['relationships'],
                    )
        return Rooms(rooms=rooms)

    async def get_room(self, room_id: str) -> Room:
        """Get a single room."""

        url = f'{Endpoint.ROOMS_URL}/{room_id}'
        room = await self._get(url)
        return Room(
            id=room['data']['id'],
            attributes=room['data']['attributes'],
            relationships=room['data']['relationships'],
        )

    async def get_pucks(self) -> Pucks:
        """Get all pucks."""

        fetched_pucks = await self._get(Endpoint.PUCKS_URL)
        pucks: dict[str, Puck] = {}

        if fetched_pucks['data']:
            for puck in fetched_pucks['data']:
                pucks[puck['id']] = Puck(
                        id=puck['id'],
                        attributes=puck['attributes'],
                        relationships=puck['relationships'],
                    )
        return Pucks(pucks=pucks)

    async def get_puck(self, puck_id: str) -> Puck:
        """Get a single puck."""

        url = f'{Endpoint.PUCKS_URL}/{puck_id}'
        puck = await self._get(url)
        return Puck(
            id=puck['data']['id'],
            attributes=puck['data']['attributes'],
            relationships=puck['data']['relationships'],
        )

    async def get_vents(self) -> Vents:
        """Get all vents."""

        fetched_vents = await self._get(Endpoint.VENTS_URL)
        vents: dict[str, Vent] = {}

        if fetched_vents['data']:
            for vent in fetched_vents['data']:
                vents[vent['id']] = Vent(
                        id=vent['id'],
                        attributes=vent['attributes'],
                        relationships=vent['relationships'],
                    )
        return Vents(vents=vents)

    async def get_vent(self, vent_id: str) -> Vent:
        """Get a single vent."""

        url = f'{Endpoint.VENTS_URL}/{vent_id}'
        vent = await self._get(url)
        return Vent(
            id=vent['data']['id'],
            attributes=vent['data']['attributes'],
            relationships=vent['data']['relationships'],
        )

    async def get_bridges(self) -> Bridges:
        """Get all bridges."""

        fetched_bridges = await self._get(Endpoint.BRIDGES_URL)
        bridges: dict[str, Bridge] = {}
        if fetched_bridges['data']:
            for bridge in fetched_bridges['data']:
                bridges[bridge['id']] = Bridge(
                    id=bridge['id'],
                    attributes=bridge['attributes'],
                    relationships=bridge['relationships'],
                )
        return Bridges(bridges=bridges)

    async def get_bridge(self, bridge_id: str) -> Bridge:
        """Get a single bridge."""

        url = f'{Endpoint.BRIDGES_URL}/{bridge_id}'
        bridge = await self._get(url)
        return Bridge(
            id=bridge['data']['id'],
            attributes=bridge['data']['attributes'],
            relationships=bridge['data']['relationships'],
        )

    async def get_thermostats(self) -> Thermostats:
        """Get all thermostats."""

        fetched_thermostats = await self._get(Endpoint.THERMOSTATS_URL)
        thermostats: dict[str, Thermostat] = {}

        if fetched_thermostats['data']:
            for thermostat in fetched_thermostats['data']:
                thermostats[thermostat['id']] = Thermostat(
                        id=thermostat['id'],
                        attributes=thermostat['attributes'],
                        relationships=thermostat['relationships'],
                    )
        return Thermostats(thermostats=thermostats)

    async def get_thermostat(self, thermostat_id: str) -> Thermostat:
        """Get a single Thermostat."""

        url = f'{Endpoint.THERMOSTATS_URL}/{thermostat_id}'
        thermostat = await self._get(url)
        return Thermostat(
            id=thermostat['data']['id'],
            attributes=thermostat['data']['attributes'],
            relationships=thermostat['data']['relationships'],
        )

    async def get_hvac_units(self) -> HVACUnits:
        """Get all HVAC units."""

        fetched_hvacs = await self._get(Endpoint.HVACS_URL)
        hvacs: dict[str, HVACUnit] = {}

        if fetched_hvacs['data']:
            for hvac in fetched_hvacs['data']:
                if hvac['attributes'].get('model-id') is not None:
                    hvacs[hvac['id']] = HVACUnit(
                            id=hvac['id'],
                            attributes=hvac['attributes'],
                            relationships=hvac['relationships'],
                        )
        return HVACUnits(hvacs=hvacs)

    async def get_hvac_unit(self, hvac_id: str) -> HVACUnit:
        """Get a single HVAC unit."""

        url = f'{Endpoint.HVACS_URL}/{hvac_id}'
        hvac = await self._get(url)
        return HVACUnit(
            id=hvac['data']['id'],
            attributes=hvac['data']['attributes'],
            relationships=hvac['data']['relationships'],
        )

    async def get_zones(self) -> Zones:
        """Get all zones."""

        fetched_zones = await self._get(Endpoint.ZONES_URL)
        zones: dict[str, Zone] = {}

        if fetched_zones['data']:
            for zone in fetched_zones['data']:
                zones[zone['id']] = Zone(
                        id=zone['id'],
                        attributes=zone['attributes'],
                        relationships=zone['relationships'],
                    )
        return Zones(zones=zones)

    async def get_zone(self, zone_id: str) -> Zone:
        """Get a single zone."""

        url = f'{Endpoint.ZONES_URL}/{zone_id}'
        zone = await self._get(url)
        return Zone(
            id=zone['data']['id'],
            attributes=zone['data']['attributes'],
            relationships=zone['data']['relationships'],
        )

    async def get_flair_data(self) -> FlairData:
        """
        Return dataclass with rooms, vents, pucks, thermostats, HVAC units,
        zones, and schedules nested within their associated structure.
        """

        users_data: dict[str, User] = {}

        response = await self.get_users()
        if response.users:
            for user in response.users:
                users_data[response.users[user].id] = User(
                    id=response.users[user].id,
                    attributes=response.users[user].attributes,
                    relationships=response.users[user].relationships,
                )

        structures_data: dict[str, Structure] = {}
        rooms_data: dict[str, Room] = {}
        pucks_data: dict[str, Puck] = {}
        vents_data: dict[str, Vent] = {}
        thermostats_data: dict[str, Thermostat] = {}
        hvac_units_data: dict[str, HVACUnit] = {}
        zones_data: dict[str, Zone] = {}
        schedules_data: dict[str, Schedule] = {}
        bridges_data: dict[str, Bridge] = {}

        response = await self.get_structures()
        if response.structures:
            for structure in response.structures:
                # Fetch related items
                related_entities = await self.fetch_all_structure_relations(response.structures[structure])

                # Related rooms
                if related_entities[0]:
                    for room in related_entities[0]:
                        rooms_data[room['id']] = Room(
                            id=room['id'],
                            attributes=room['attributes'],
                            relationships=room['relationships'],
                        )

                # Related pucks
                if related_entities[1]:
                    for puck in related_entities[1]:
                        puck_object = Puck(
                            id=puck['id'],
                            attributes=puck['attributes'],
                            relationships=puck['relationships'],
                            current_reading=None
                        )
                        if not puck['attributes']['inactive']:
                            get_reading = await self.get_related(puck_object, 'current-reading')
                            attributes = get_reading['attributes']
                        else:
                            attributes = {}
                        setattr(puck_object, 'current_reading', attributes)
                        pucks_data[puck['id']] = puck_object

                # Related vents
                if related_entities[2]:
                    for vent in related_entities[2]:
                        vent_object = Vent(
                            id=vent['id'],
                            attributes=vent['attributes'],
                            relationships=vent['relationships'],
                            current_reading=None
                        )
                        if not vent['attributes']['inactive']:
                            get_reading = await self.get_related(vent_object, 'current-reading')
                            attributes = get_reading['attributes']
                        else:
                            attributes = {}
                        setattr(vent_object, 'current_reading', attributes)
                        vents_data[vent['id']] = vent_object

                # Related thermostats
                if related_entities[3]:
                    for thermostat in related_entities[3]:
                        thermostats_data[thermostat['id']] = Thermostat(
                            id=thermostat['id'],
                            attributes=thermostat['attributes'],
                            relationships=thermostat['relationships'],
                        )

                # Related HVAC units
                if related_entities[4]:
                    for hvac_unit in related_entities[4]:
                        hvac_units_data[hvac_unit['id']] = HVACUnit(
                            id=hvac_unit['id'],
                            attributes=hvac_unit['attributes'],
                            relationships=hvac_unit['relationships'],
                        )

                # Related zones
                if related_entities[5]:
                    for zone in related_entities[5]:
                        zones_data[zone['id']] = Zone(
                            id=zone['id'],
                            attributes=zone['attributes'],
                            relationships=zone['relationships'],
                        )

                # Related schedules
                if related_entities[6]:
                    for schedule in related_entities[6]:
                        schedules_data[schedule['id']] = Schedule(
                            id=schedule['id'],
                            attributes=schedule['attributes'],
                            relationships=schedule['relationships'],
                        )

                # Related Bridges
                if related_entities[7]:
                    for bridge in related_entities[7]:
                        bridge_object = Bridge(
                            id=bridge['id'],
                            attributes=bridge['attributes'],
                            relationships=bridge['relationships'],
                            current_reading=None
                        )
                        if not bridge['attributes']['inactive']:
                            get_reading = await self.get_related(bridge_object, 'current-reading')
                            attributes = get_reading['attributes']
                        else:
                            attributes = {}
                        setattr(bridge_object, 'current_reading', attributes)
                        bridges_data[bridge['id']] = bridge_object


                structures_data[response.structures[structure].id] = Structure(
                        id=response.structures[structure].id,
                        attributes=response.structures[structure].attributes,
                        relationships=response.structures[structure].relationships,
                        rooms=rooms_data,
                        pucks=pucks_data,
                        vents=vents_data,
                        bridges=bridges_data,
                        thermostats=thermostats_data,
                        hvac_units=hvac_units_data,
                        zones=zones_data,
                        schedules=schedules_data,
                )
        return FlairData(users=users_data, structures=structures_data )


    async def get_related(self, flair_object, related_type: str) -> list[int]:
        """Get vents, rooms, pucks, etc. related to the object."""

        link = flair_object.relationships[related_type]['links']['related']
        response = await self._get(link)
        return response['data']

    async def fetch_all_structure_relations(self, flair_object: Structure) -> list:
        """
        Parallel request are made to all related endpoints for a single structure.
        Returns a list containing rooms, pucks, vents, thermostats, HVAC units, zones, schedules,
        and bridges related to said structure. This function is called by the get_flair_data function.
        """

        results = await asyncio.gather(*[
            self.get_related(flair_object, 'rooms'),
            self.get_related(flair_object, 'pucks'),
            self.get_related(flair_object, 'vents'),
            self.get_related(flair_object, 'thermostats'),
            self.get_related(flair_object, 'hvac-units'),
            self.get_related(flair_object, 'zones'),
            self.get_related(flair_object, 'schedules'),
            self.get_related(flair_object, 'bridges')
            ],
        )
        return results

    async def create(self, resource_type: str, attributes: dict[str, Any], relationships: dict[str, Any]) -> dict[str, Any]:
        """Create a new Flair room. Other scenarios currently untested."""

        await self.check_token()
        headers = {
            "content-type": 'application/json',
            "authorization": f'Bearer {self.token}'
        }

        request_data = {
            "data": {
                "type": resource_type,
                "attributes": attributes,
                "relationships": relationships
            }
        }
        request_url = f'/api/{resource_type}'
        return await self._post(request_url, headers, request_data)

    async def delete(self, resource_type: str, item_id: str) -> None:
        """Delete a Flair room. Other scenarios currently untested."""

        request_url = f'/api/{resource_type}/{item_id}'
        return await self._delete(request_url)

    async def update(self, resource_type: str, item_id: str, attributes: dict[str, Any], relationships: dict[str, Any]) -> dict[str, Any]:
        """Set structure mode, structure system mode, vent % open, select schedule, etc."""

        request_data = {
            "data": {
                "type": resource_type,
                "attributes": attributes,
                "relationships": relationships
            }
        }
        request_url = f'/api/{resource_type}/{item_id}'
        return await self._patch(request_url, request_data)

    async def _create_get_header(self) -> dict[str, str]:
        """Create header for all GET calls."""

        headers = {
            "content-type": Header.CONTENT_ENCODED,
            "accept": Header.ACCEPT,
            "authorization": f'Bearer {self.token}'
        }
        return headers

    async def _create_json_header(self) -> dict[str, str]:
        """Create json content-type header."""

        headers = {
            "content-type": Header.CONTENT_JSON,
            "authorization": f'Bearer {self.token}'
        }
        return headers

    async def _post(self, endpoint: str, headers: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]:
        """Make POST call to Flair servers."""

        if headers['content-type'] == 'application/json':
            async with self._session.post(
                    url=f'{Endpoint.BASE_URL}{endpoint}', headers=headers,
                    json=data, timeout=self.timeout) as resp:
                return await self._response(resp)
        else:
            async with self._session.post(
                    url=f'{Endpoint.BASE_URL}{endpoint}', headers=headers,
                    data=data, timeout=self.timeout) as resp:
                return await self._response(resp)

    async def _get(self, endpoint: str, data: dict[str, Any] = None) -> dict[str, Any]:
        """Make GET call to Flair servers."""

        data = data if data else {}
        await self.check_token()
        headers = await self._create_get_header()
        async with self._session.get(
                url=f'{Endpoint.BASE_URL}{endpoint}', headers=headers,
                data=data, timeout=self.timeout) as resp:
            return await self._response(resp)

    async def _delete(self, endpoint: str) -> None:
        """Make DELETE call to Flair servers."""

        await self.check_token()
        headers = await self._create_json_header()
        async with self._session.delete(
                url=f'{Endpoint.BASE_URL}{endpoint}', headers=headers,
                timeout=self.timeout) as resp:
            return await self._response(resp)

    async def _patch(self, endpoint: str, data: dict[str, Any]) -> dict[str, Any]:
        """Make PATCH call to Flair servers."""

        await self.check_token()
        headers = await self._create_json_header()
        async with self._session.patch(
                url=f'{Endpoint.BASE_URL}{endpoint}', headers=headers,
                json=data, timeout=self.timeout) as resp:
            return await self._response(resp)

    @staticmethod
    async def _response(resp: ClientResponse) -> dict[str, Any] | None:
        """Check response for any errors.

        If no errors are encountered in the response, the original response
        is returned.
        """

        if resp.status == 204:
            return None
        elif resp.status == 504:
            raise FlairError(resp)
        else:
            try:
                response: dict[str, Any] = await resp.json()
                if resp.status != 200:
                    if resp.reason == Reason.CREATED:
                        return response
                    if resp.reason == Reason.FORBIDDEN:
                        raise FlairAuthError(f'{response["errors"][0]["detail"]}')
                    if resp.reason == Reason.UNPROC_ENTITY:
                        base = response['errors'][0]
                        raise FlairError(f'{base["title"]}: {base["detail"]}')
                    if 'error' in response:
                        if response['error'] == Reason.INVALID_CLIENT:
                            raise FlairAuthError('Invalid Client ID or Secret provided')
                else:
                    return response
            except ContentTypeError as cte:
                text = await resp.text()
                raise FlairError(f'Flair server response content-type is not json: {text}') from cte
            except (KeyError, ValueError) as e:
                raise FlairError(f'Flair API error: {e}') from e
