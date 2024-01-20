

def test_outputs_get(client):
    response = client.get("/api/outputs")
    assert b'{"0":"off","1":"off","2":"off","3":"off","4":"off","5":"off","6":"off","7":"off"}' in response.data
    assert response.status_code == 200


def test_output_get(client):
    response = client.get("/api/output/0")
    assert b'off' in response.data
    assert response.status_code == 200


def test_output_put_on(client):
    response = client.put("/api/output/0/on")
    assert b'on' in response.data
    assert response.status_code == 200


def test_output_put_off(client):
    response = client.put("/api/output/0/off")
    assert b'off' in response.data
    assert response.status_code == 200


def test_output_put_toggle_on(client):
    response = client.put("/api/output/0/toggle")
    assert b'on' in response.data
    assert response.status_code == 200


def test_output_put_toggle_off(client):
    response = client.put("/api/output/0/toggle")
    assert b'off' in response.data
    assert response.status_code == 200


def test_output_put_invalid(client):
    response = client.put("/api/output/0/invalid")
    assert b'{"message": "Invalid action specified. Must be \'on\', \'off\' or \'toggle\'"}\n' in response.data
    assert response.status_code == 400
