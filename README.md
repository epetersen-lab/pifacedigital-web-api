# PiFaceDigital-Web-API

## Description
Web API for interacting with the PiFace Digital expansion board on Raspberry Pi, written in Python.


## INPUTS

Endpoints for retrieveing the state of the input pins.

### Get state of all inputs
**URL** : `/api/inputs`  
**Method** : `GET`  
**Content example** : `{"0":"off","1":"off","2":"off","3":"off","4":"off","5":"off","6":"off","7":"off"}`  
**Status code** :
* 200 - Success

### Get specific input pin
**URL** : `/api/input/<pin>`  
**Method** : `GET`  
**Path parameter** :
* pin - Id of the input pin to retrieve the state for (0-7)

**Content** : `"off"` or `"on"`  
**Status code** :
* 200 - Success
* 400 - Invalid pin parameter

## OUTPUTS
Endpoints for getting ans setting the state of the output pins.

### Get state of all output pins
**URL** : `/api/outputs`  
**Method** : `GET`  
**Content example** : `{"0":"off","1":"off","2":"off","3":"off","4":"off","5":"off","6":"off","7":"off"}`  
**Status code** :
* 200 - Success

### Get state for specific output pin
**URL** : `/api/output/<pin>`  
**Method** : `GET`  
**Path parameter** :
* pin - Id of the output pin to retrieve the state for (0-7)

**Content example** : `"off"` or `"on"`  
**Status code** :
* 200 - Success
* 400 - Invalid pin parameter

### Set state for specific output pin
**URL** : `/api/output/<pin>/<state>`
**Method** : `PUT`  
**Path parameter** :
* pin - Id of the selected output pin (0-7)
* state - New state for the selected pin. `"on"`, `"off"` or `"toggle"`

**Content** : `"off"` or `"on"`  
**Status code** :  
* 200 - Success
* 400 - Invalid pin or state parameter

