import pifacedigitalio
from flask import Flask, jsonify
from flask_restful import Api, Resource

pifacedigital = pifacedigitalio.PiFaceDigital()


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    api.add_resource(PiFaceOutputs, "/outputs", methods=["GET"])
    api.add_resource(PiFaceOutput, "/output/<int:output_pin>", methods=["GET"])
    api.add_resource(PiFaceOutputSet, "/output/<int:output_pin>/<string:state>", methods=["PUT"])
    api.add_resource(PiFaceInput, "/input/<int:input_pin>", methods=["GET"])
    api.add_resource(PiFaceInputs, "/inputs", methods=["GET"])
    return app


def onoff(value):
    if value == 1:
        return "on"
    return "off"


def message(text):
    return {"message": text}


class PiFaceOutput(Resource):
    def get(self, output_pin):
        if output_pin < 0 or output_pin > 7:
            return message("Invalid output pin specified. Must be a value between 0-7"), 400
        return onoff(pifacedigital.output_pins[output_pin].value)


class PiFaceOutputSet(Resource):
    def put(self, output_pin, state):
        if output_pin < 0 or output_pin > 7:
            return message("Invalid output pin specifed. Must be a value between 0-7"), 400

        if state == "on":
            pifacedigital.output_pins[output_pin].turn_on()
            return onoff(pifacedigital.output_pins[output_pin].value)

        if state == "off":
            pifacedigital.output_pins[output_pin].turn_off()
            return onoff(pifacedigital.output_pins[output_pin].value)

        if state == "toggle":
            pifacedigital.output_pins[output_pin].toggle()
            return onoff(pifacedigital.output_pins[output_pin].value)

        return message("Invalid action specified. Must be 'on', 'off' or 'toggle'"), 400


class PiFaceOutputs(Resource):
    def get(self):
        output_pins = {}
        for output_pin in range(0, 8):
            output_pins[output_pin] = onoff(pifacedigital.output_pins[output_pin].value)
        return jsonify(output_pins)


class PiFaceInput(Resource):
    def get(self, input_pin):
        if input_pin < 0 or input_pin > 7:
            return message("Invalid input pin specified. Must be a value between 0-7"), 400
        return onoff(pifacedigital.input_pins[input_pin].value)


class PiFaceInputs(Resource):
    def get(self):
        input_pins = {}
        for input_pin in range(0, 8):
            input_pins[input_pin] = onoff(pifacedigital.input_pins[input_pin].value)
        return jsonify(input_pins)


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
