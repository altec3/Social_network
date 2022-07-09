import pytest
import wsgi


@pytest.fixture()
def test_client():
    app = wsgi.app
    return app.test_client()


@pytest.fixture()
def correct_keys():
    return ['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count']
