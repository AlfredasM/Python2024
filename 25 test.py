import pytest
from main import


# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_blog.db'
#     client = app.test_client()
#     with app.app_context():
#         db.create_all()
#     yield client
#
#     with app.app_context():
#         db.drop_all()
#
#
# def test_create_post(client):
#     response = client.post('/posts', json={'title': 'test title', 'content': 'test content'})
#     assert response.status_code == 201
#     assert response.json['post']['title'] == 'test title'
#
#
# def test_get_posts(client):
#     client.post('/posts', json={'title': 'test title', 'content': 'test content'})
#     response = client.get('/posts/1')
#     assert response.status_code == 200
#     assert response.json['title'] == 'test title'
#
#
# def test_delete_post(client):
#     client.post('/posts', json={'title': 'test title', 'content': 'test content'})
#     delete_resp = client.delete('/posts/1')
#     assert delete_resp.status_code == 200
#     assert delete_resp.json['message'] == 'Post deleted'
#
#     get_response = client.get('/posts/1')
#     assert get_response.status_code == 404

