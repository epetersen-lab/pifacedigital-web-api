

def test_outputs_get(client):
    response = client.get("/api/outputs")
    assert b'{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0}' in response.data
    assert response.status_code == 200


def test_output_get(client):
    response = client.get("/api/output/0", headers={"Content-Type": "application/json"})
    assert b'0' in response.data
    assert response.status_code == 200


def test_output_post_on(client):
    response = client.post("/api/output/0", data="1", headers={"Content-Type": "application/json"})
    assert b'1' in response.data
    assert response.status_code == 200


def test_output_post_off(client):
    response = client.post("/api/output/0", data="0", headers={"Content-Type": "application/json"})
    assert b'0' in response.data
    assert response.status_code == 200