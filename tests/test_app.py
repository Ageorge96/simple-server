def test_app(web_client):
    response = web_client.get('/')
    assert response.status_code == 200

def test_response(web_client):
    response = web_client.get("response")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hey, Andre! How's you day?"