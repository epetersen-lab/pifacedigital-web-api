# PiFaceDigital-Web-API

Web API for interacting with the PiFaceDigital expansion board on Raspberry Pi,  
written in Python using Flask and Flask-RESTful.  

## Table of content
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [API Documentation](#api-documentation)
   1. [Input pins](#input-pins)
   2. [Output pins](#output-pins)
4. [Home Assistant integration](#home-assistant-integration)
   1. [Integrate input pins](#integrate-input-pins)
   2. [Integrate output pins](#integrate-output-pins)
5. [References](#references)

## Installation
```sh
make dist
sudo pip3 install -U dist/pifacedigital_web_api-<version>-py3-none-any.whl
```
#### Install and enable as systemd service
```sh
sudo make systemd-install
```
#### Remove the systemd service
```sh
sudo make systemd-remove
```

## Configuration
The default port for accessing the API is TCP/8080.
The port can be changed in the systemd service file located  
at `/etc/systemd/system/pifacedigital-web-api.service` 


## API Documentation
A RESTful API is provided for interacting with IO-pins of the PiFaceDigital.  
The state of the input can be read. Output pins can be switched on and off.


### Input pins

Endpoints for retrieving the state of the input pins.

#### Get state of all inputs
**URL** : `/api/inputs`  
**Method** : `GET`  
**Content example** : `{"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0}`  
**Status code** :
* 200 - Success

#### Get specific input pin
**URL** : `/api/input/<pin>`  
**Method** : `GET`  
**Path parameter** :
* pin - Id of the input pin to retrieve the state for (0-7)

**Content** : `0` or `1`  
**Status code** :
* 200 - Success
* 400 - Invalid pin parameter

### Output pins
Endpoints for getting and setting the state of the output pins.

#### Get state of all output pins
**URL** : `/api/outputs`  
**Method** : `GET`  
**Content example** : `{"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0}`  
**Status code** :
* 200 - Success

#### Get state for specific output pin
**URL** : `/api/output/<pin>`  
**Method** : `GET`  
**Path parameter** :
* pin - Id of the output pin to retrieve the state for (0-7)

**Content example** : `0` or `1`  
**Status code** :
* 200 - Success
* 400 - Invalid pin parameter

#### Set state for specific output pin
**URL** : `/api/output/<pin>`  
**Method** : `POST`  
**Data**: `0` or `1`  
**Path parameter** :
* pin - Id of the selected output pin (0-7)

**Content** : `0` or `1`  
**Status code** :  
* 200 - Success
* 400 - Invalid pin or state parameter


## Home Assistant integration
The project can integrate to [Home Assistant](https://www.home-assistant.io),
so it is possible to use the state information and control the outputs in your automations.  


#### Integrate input pins
The state of an input pin can be retrieved by Home Assistant via the  
RESTful binary sensor. Input pin0 and pin1 can be monitored by entering the following to your  
`configuration.yaml`.  The example below will make a request to the API every 10 seconds,    
so to be sure of detecting a state change, it has to remain in that state at least  
this amount of time. This makes it unfit for certain use cases where the state changes  
only briefly, like the behaviour of a push button.

```
# Input pin0
binary_sensor:
  - platform: rest
    name: pifacedigital_input_0
    unique_id: pifacedigital_input_0
    resource: http://<HOST>:8080/api/input/0
    scan_interval: 10

# Input pin1
binary_sensor:
  - platform: rest
    name: pifacedigital_input_1
    unique_id: pifacedigital_input_1
    resource: http://<HOST>:8080/api/input/1
    scan_interval: 10
```

#### Integrate output pins
The state of output pins can be controlled and retrieved by Home Assistant  
via the RESTful Switch integration.  
This example shows how to add output pin0 and pin1 to your `configuration.yaml` 

```
# Output pin1
switch:
  - platform: rest
    name: pifacedigital_output_0
    unique_id: pifacedigital_output_0
    resource: http://<HOST>:8080/api/output/0
    is_on_template: "{{ value |int == 1 }}"
    body_on: '1'
    body_off: '0'
    headers:
      Content-Type: application/json
    scan_interval: 10

# Output pin1
  - platform: rest
    name: pifacedigital_output_1
    unique_id: pifacedigital_output_1
    resource: http://<HOST>:8080/api/output/1
    is_on_template: "{{ value |int == 1 }}"
    body_on: '1'
    body_off: '0'
    headers:
      Content-Type: application/json
    scan_interval: 10
```

## References
 - [PiFace Digital I/O's documentation](https://pifacedigitalio.readthedocs.io/)  
 - [Flask documentation](https://flask.palletsprojects.com/)  
 - [Flask-RESTful documentation](https://flask-restful.readthedocs.io/)  
 - [Home Assistant](https://www.home-assistant.io)  