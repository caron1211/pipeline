import json

from server import app


def test_home_page():
    """
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"carmel" in response.data


def test_post_request():
    response = app.test_client().post('user/alon', data=json.dumps({'name': 'alon'}), content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert data['name'] == 'alon'
    assert data['age'] == 12

