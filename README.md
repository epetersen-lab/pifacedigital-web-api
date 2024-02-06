# PiFaceDigital-Web-API

## Description
Web API for interacting with the PiFaceDigital expansion board on Raspberry Pi,
written in Python using Flask and Flask-RESTful.  

The default port for accessing the API is TCP/8080.

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

## API Documentation
A RESTful API is provided for interacting with IO-pins of the PiFaceDigital.  
The state of the input can be read. Output pins can be switched on and off.


### INPUTS

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

### OUTPUTS
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
