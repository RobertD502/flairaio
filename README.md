# Flairaio

Asynchronous Python library for Flair's API using **OAuth 2.0 Authentication**.

This package provides an API client for the [Flair API](https://documenter.getpostman.com/view/5353571/TzsbKTAG#intro) 
to be used with **OAuth 2.0** credentials generated by Flair. For API access, please [contact Flair Support](https://support.flair.co/hc/en-us/requests/new)
with the email address associated with your registered Flair account.

## Installation

### PyPI
```
pip3 install flairaio
```


This package depends on [aiohttp](https://docs.aiohttp.org/en/stable/) and requires `Python 3.7` or greater.

## Usage

### Creating Client

```python
import asyncio
from flairaio import FlairClient
from aiohttp import ClientSession

async def main():
    async with ClientSession() as session:
    
        # Create a client using OAuth 2.0 client_id and client_secret
        client = FlairClient('client_id', 'client_secret', session)
        

        ###################################################################################
        Examples within the examples section utilize the FlairClient instance created above
        ###################################################################################

        
        
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Examples
&nbsp; 
### Retrieving objects of interest
___
###

<details>
  <summary> <b>Users</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "Users" and "User" Data Classes


# Retrieve all users.
users = await client.get_users()

# Retrieve a specific user. Note: user_id is the specific user's ID as a string.
user = await client.get_user(user_id='1')


```
</details>

&nbsp;

<details>
  <summary> <b>Structures</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "Structures" and "Structure" Data Classes


# Retrieve all structures.
structures = await client.get_structures()

# Retrieve a specific structure. Note: structure_id is the specific structure's ID as a string.
structure = await client.get_structure(structure_id='1')

```
</details>

&nbsp;

<details>
  <summary> <b>Rooms</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "Rooms" and "Room" Data Classes


# Retrieve all rooms.
rooms = await client.get_rooms()

# Retrieve a specific room. Note: room_id is the specific room's ID as a string.
room = await client.get_room(room_id='1')

```
</details>

&nbsp;

<details>
  <summary> <b>Pucks</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "Pucks" and "Puck" Data Classes


# Retrieve all pucks.
pucks = await client.get_pucks()

# Retrieve a specific puck. Note: puck_id is the specific puck's ID as a string.
puck = await client.get_puck(puck_id='1')



```
</details>

&nbsp;

<details>
  <summary> <b>Vents</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "Vents" and "Vent" Data Classes


# Retrieve all vents.
vents = await client.get_vents()

# Retrieve a specific vent. Note: vent_id is the specific vent's ID as a string.
vent = await client.get_vent(vent_id='1')



```
</details>

&nbsp;

<details>
  <summary> <b>Bridges</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "Bridges" and "Bridge" Data Classes


# Retrieve all bridges.
bridges = await client.get_bridges()

# Retrieve a specific bridge. Note: bridge_id is the specific bridge's ID as a string.
bridge = await client.get_bridge(bridge_id='1')



```
</details>

&nbsp;

<details>
  <summary> <b>Thermostats</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "Thermostats" and "Thermostat" Data Classes


# Retrieve all thermostats.
thermostats = await client.get_thermostats()

# Retrieve a specific thermostat. Note: thermostat_id is the specific thermostat's ID as a string.
thermostat = await client.get_thermostat(thermostat_id='1')



```
</details>

&nbsp;

<details>
  <summary> <b>HVAC Units</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "HVACUnits" and "HVACUnit" Data Classes


# Retrieve all HVAC units.
hvac_units = await client.get_hvac_units()

# Retrieve a specific HVAC unit. Note: hvac_id is the specific HVAC unit's ID as a string.
hvac_unit = await client.get_hvac_unit(hvac_id='1')



```
</details>

&nbsp;

<details>
  <summary> <b>Zones</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "Zones" and "Zone" Data Classes


# Retrieve all zones.
zones = await client.get_zones()

# Retrieve a specific zone. Note: zone_id is the specific zone's ID as a string.
zone = await client.get_zone(zone_id='1')



```
</details>

&nbsp;

<details>
  <summary> <b>Getting all Flair Data</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# See model.py for details regarding "FlairData" Data Class

# The resulting FlairData instance will contain an instance of "Users" and an instance of "Structures" which 
# contains instances of "Structure" created for every structure associated with your account. Within each Structure,
# you will find its id, attributes, relationships, as well as all rooms, pucks, vents, thermostats, HVAC units, and zones
# associated with said structure - each of these also contains their id, attributes, and relationships. As a bonus, the
# get_flair_data method also fetches the current reading endpoints for pucks and vents.


# Retrieve all flair data.
flair_data = await client.get_flair_data()



```
</details>

&nbsp;

### Retrieving Related Items
___

#### *** See Related Endpoints for available related links.
###

<details>
  <summary> <b>Getting related data</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# You need to create an instance of the object of interest prior to retrieving its related item(s).


# Create a Puck instance for a specific puck. Note: puck_id is the specific puck's ID as a string.
puck = await client.get_puck(puck_id='1')

# Retrieve "current-reading" for puck
current_reading = await client.get_related(flair_object=puck, related_type='current_reading')



```
</details>

&nbsp;

### Creating
___

###

<details>
  <summary> <b>Creating New Room</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# Content of attributes and relationships dictionaries will depend on what is being created.


# Create attributes dictionary for new room.
attributes = {
    "name": "My New Flair Room"
}

# Creat new room "My New Flair Room"
await client.create(resource_type='rooms', attributes=attributes, relationships={})



```
</details>

&nbsp;

### Deleting
___

###

<details>
  <summary> <b>Deleting Room</b> (<i>click to expand</i>)</summary>
  <!---->

```python

# Deleting a room with an id of '1234'
await client.delete(resource_type='rooms', item_id='1234')

```
</details>

&nbsp;

### Updating
___

###

<details>
  <summary> <b>Opening Vent</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# Content of attributes and relationships dictionaries will depend on what is being updated.
# The example below is fully opening a specific Flair vent


# create attributes dictionary
attributes = {
    "percent-open": 100
}

# Fully open the vent
await client.update(resource_type='vents', item_id='1', attributes=attributes, relationships={})


```
</details>

&nbsp;

<details>
  <summary> <b>Setting Bridge LED Brightness</b> (<i>click to expand</i>)</summary>
  <!---->

```python
# Content of attributes and relationships dictionaries will depend on what is being updated.
# The example below is setting the LED brightness for a specific Flair Bridge.
# Note: Flair Bridge LED brightness accepts an int between, and including, 20-100


# create attributes dictionary
attributes = {
    "led-brightness": 50
}

# Set LED brightness
await client.update(resource_type='bridges', item_id='1', attributes=attributes, relationships={})


```
</details>

&nbsp;

<details>
  <summary> <b>Setting HVAC Unit Mode</b> (<i>click to expand</i>)</summary>
  <!---->

### Note:
#### * If structure is set to Manual mode: HVAC mode, temp, swing, and fan speed can only be set when the unit is powered on.

#### * If structure is set to Auto mode: Only swing and fan speed can be set.

#### * Fan speed: if structure is set to Manual mode, changing fan speed requires updating the attribute `"fan-speed"`. Changing fan speed with structure in Auto mode requires updating the attribute `"default-fan-speed"`.

#### * Swing: If structure is set to Manual mode, changing swing requires updating the attribute `"swing"`. Changing swing with structure in Auto mode requires updating the attribute `"swing-auto"`.
#
```python
# Content of attributes and relationships dictionaries will depend on what is being updated.
# The example below is setting the HVAC Unit mode to Cool.


# create attributes dictionary
attributes = {
    "mode": 'Cool'
}

# Update HVAC unit's mode to Cool
await client.update(resource_type='hvac-units', item_id='1', attributes=attributes, relationships={})


```
</details>

&nbsp;

## Available Related Endpoints


<div align="center">
<table>
  <tbody>
    <tr>
      <th>Resource Type</th>
      <th align="center">Related</th>
    </tr>
       <tr>
      <td align="center">Bridge</td>
      <td>
        <ul>
          <li>structure</li>
          <li>current-state</li>
          <li>hardware-version</li>
          <li>current-reading</li>
          <li>room</li>
          <li>sensor-readings</li>
          <li>bridge-states</li>
        </ul>
    </tr>
       <tr>
      <td align="center">HVAC Unit</td>
      <td>
        <ul>
          <li>puck</li>
          <li>current-state</li>
          <li>hvac-unit-states</li>
          <li>structure</li>
          <li>zone</li>
          <li>plug</li>
          <li>integration-structure</li>
          <li>make</li>
          <li>room</li>
        </ul>
    </tr>
    <tr>
      <td align="center">Puck</td>
      <td>
        <ul>
          <li>room</li>
          <li>hardware-version</li>
          <li>hvac-units</li>
          <li>puck-states</li>
          <li>closest-vents</li>
          <li>beacon-sightings</li>
          <li>current-reading</li>
          <li>structure</li>
          <li>sensor-readings</li>
          <li>current-state</li>
        </ul>
    </tr>
       <tr>
      <td align="center">Room</td>
      <td>
        <ul>
          <li>remote-sensors</li>
          <li>thermostat</li>
          <li>structure</li>
          <li>occupants</li>
          <li>pucks</li>
          <li>vents</li>
          <li>hvac-units</li>
          <li>room-states</li>
          <li>bridges</li>
          <li>current-conclusions</li>
          <li>puck-apps</li>
          <li>zones</li>
          <li>plugs</li>
          <li>occupancy-conclusions</li>
          <li>room-auto-conclusions</li>
        </ul>
    </tr>
    <tr>
      <td align="center">Structure</td>
      <td>
        <ul>
          <li>admin-users</li>
          <li>release-approvals</li>
          <li>default-zone</li>
          <li>remote-sensors</li>
          <li>schedules</li>
          <li>hvac-units</li>
          <li>demand-response-program-enrollments</li>
          <li>weather-readings</li>
          <li>hvac-unit-groups</li>
          <li>beacon-sightings</li>
          <li>plugs</li>
          <li>alerts</li>
          <li>structure-states</li>
          <li>current-conclusions</li>
          <li>rooms</li>
          <li>geofence-events</li>
          <li>pucks</li>
          <li>releases</li>
          <li>bridges</li>
          <li>licenses</li>
          <li>occupancy-conclusions</li>
          <li>thermostats</li>
          <li>integration-structures</li>
          <li>viewer-users</li>
          <li>supported-device-brands</li>
          <li>geofences</li>
          <li>current-weather</li>
          <li>active-schedule</li>
          <li>current-state</li>
          <li>ui-notifications</li>
          <li>zones</li>
          <li>invitations</li>
          <li>vents</li>
          <li>plug-invites</li>
          <li>editor-users</li>
          <li>devices</li>
          <li>puck-oauth-apps</li>
        </ul>
    </tr>
       <tr>
      <td align="center">Thermostat</td>
      <td>
        <ul>
          <li>current-state</li>
          <li>integration-structure</li>
          <li>zone</li>
          <li>remote-sensor</li>
          <li>thermostat-states</li>
          <li>structure</li>
          <li>room</li>
        </ul>
    </tr>
    <tr>
      <td align="center">User</td>
      <td>
        <ul>
          <li>networks</li>
          <li>unfinished-setup-structure</li>
          <li>integrations</li>
          <li>ui-notifications</li>
          <li>accessible-structures</li>
          <li>editable-structures</li>
          <li>received-invitations</li>
          <li>default-structure</li>
          <li>primary-device</li>
          <li>structures</li>
          <li>adminable-structures</li>
          <li>viewable-structures</li>
          <li>devices</li>
          <li>puck-oauth-apps</li>
        </ul>
    </tr>
       <tr>
      <td align="center">Vent</td>
      <td>
        <ul>
          <li>current-reading</li>
          <li>current-state</li>
          <li>sensor-readings</li>
          <li>closest-puck</li>
          <li>room</li>
          <li>vent-states</li>
          <li>structure</li>
        </ul>
    </tr>
       <tr>
      <td align="center">Zone</td>
      <td>
        <ul>
          <li>rooms</li>
          <li>zone-auto-conclusions</li>
          <li>structure</li>
          <li>thermostat</li>
          <li>hvac-unit</li>
        </ul>
    </tr>
  </tbody>
</table>
</div>
