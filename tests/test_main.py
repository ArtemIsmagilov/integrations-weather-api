def test_ping(client):
    response = client.get("/root/ping")
    assert response.status_code == 200


def test_search(client):
    response = client.get("/cities/search?q=То")
    assert response.status_code == 200
    assert response.json()[0]["title"] == "Тольятти"

    response = client.get("/cities/search?q=Сама")
    assert response.status_code == 200
    assert response.json()[0]["title"] == "Самара"

    response = client.get("/cities/search?q=asdkjlkasd")
    assert response.status_code == 404


def test_temperature(client, mock_pool):
    response = client.get("/cities/temperature/asdasdadad")
    assert response.status_code == 404

    response = client.get("/cities/temperature/Самара")
    assert response.status_code == 200

    response = client.get("/cities/temperature/Тольятти")
    assert response.status_code == 200

    # result from memcached
    response = client.get("/cities/temperature/Самара")
    assert response.status_code == 200

    mock_pool.delete("Самара")
    mock_pool.delete("Тольятти")


def test_web(client):
    # test plug with web interface
    response = client.get("/web/items/1")
    assert response.status_code == 200
