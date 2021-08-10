

def test_app_is_created(app):
    assert app.name == "delivery.app"


def test_config_is_loader(config):
    assert config['DEBUG'] is False


def test_request_return_404(client):
    assert client.get('/').status_code == 404


