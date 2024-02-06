import pifacedigitalio
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

pifacedigital = pifacedigitalio.PiFaceDigital()


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    api.add_resource(PiFaceOutputs, "/api/outputs", methods=["GET"])
    api.add_resource(PiFaceOutput, "/api/output/<int:output_pin>", methods=["GET", "POST"])
    api.add_resource(PiFaceInput, "/api/input/<int:input_pin>", methods=["GET"])
    api.add_resource(PiFaceInputs, "/api/inputs", methods=["GET"])
    return app


def message(text):
    return {"message": text}


class PiFaceOutput(Resource):
    def get(self, output_pin):
        if output_pin < 0 or output_pin > 7:
            return message("Invalid output pin specified. Must be a value between 0-7"), 400
        return int(pifacedigital.output_pins[output_pin].value)

    def post(self, output_pin):
        if request.json == 0:
            pifacedigital.output_pins[output_pin].turn_off()
        if request.json == 1:
            pifacedigital.output_pins[output_pin].turn_on()
        return pifacedigital.output_pins[output_pin].value


class PiFaceOutputs(Resource):
    def get(self):
        output_pins = {}
        for output_pin in range(0, 8):
            output_pins[output_pin] = pifacedigital.output_pins[output_pin].value
        return jsonify(output_pins)


class PiFaceInput(Resource):
    def get(self, input_pin):
        if input_pin < 0 or input_pin > 7:
            return message("Invalid input pin specified. Must be a value between 0-7"), 400
        return pifacedigital.input_pins[input_pin].value


class PiFaceInputs(Resource):
    def get(self):
        input_pins = {}
        for input_pin in range(0, 8):
            input_pins[input_pin] = pifacedigital.input_pins[input_pin].value
        return jsonify(input_pins)


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)
