

def test_inputs_get(client):
    response = client.get("/api/inputs")
    assert b'{"0":"off","1":"off","2":"off","3":"off","4":"off","5":"off","6":"off","7":"off"}' in response.data
    assert response.status_code == 200


def test_input(client):
    response = client.get("/api/input/0")
    assert b'"off"' in response.data
    assert response.status_code == 200


def test_input_invalid(client):
    response = client.get("/api/input/12")
    assert b'{"message": "Invalid input pin specified. Must be a value between 0-7"}\n' in response.data
    assert response.status_code == 400
