import pytest

from ..app.app import create_app


@pytest.fixture(scope="module")
def app():
    """New Instance of app to tests"""
    return create_app()

@pytest.fixture(scope="function")
def client(app):
    app.testing = True
    return app.test_client()