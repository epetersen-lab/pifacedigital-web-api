

def test_inputs_get(client):
    response = client.get("/api/inputs")
    assert b'{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0}' in response.data
    assert response.status_code == 200


def test_input(client):
    response = client.get("/api/input/0")
    assert b'0' in response.data
    assert response.status_code == 200


def test_input_invalid(client):
    response = client.get("/api/input/12")
    assert b'{"message": "Invalid input pin specified. Must be a value between 0-7"}\n' in response.data
    assert response.status_code == 400
