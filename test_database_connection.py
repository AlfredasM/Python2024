import pytest
import psycopg2
from db_config import db_config


# @pytest.fixture(scope="module")
# def db_connection():
#     conn = None
#     try:
#         conn = psycopg2.connect(**db_config)
#         yield conn  # leidzia atlikti veiksmus, leidzia kontrole testui, naudtoti faila
#     finally:
#         if conn is not None:
#             conn.close()
#
#
# def test_postgres_connection(db_connection):
#     assert db_connection is not None
#     assert db_connection.status == psycopg2.extensions.STATUS_READY

# @pytest.fixture(params=[1, 2, 3, 4, 5])
# def skaicius(request):
#     return request.param
#
#
# def test_is_dvieju(skaicius):
#     assert skaicius % 2 == 0 or skaicius % 2 == 1


# @pytest.fixture(params=['hello', 'pytest', 'world'])
# def word(request):
#     return request.param
#
# def test_word_contains_py(word):
#     assert 'py' in word or 'py' not in word

# @pytest.fixture(params=[1, 2, 3, -1])
# def skaicius(request):
#     return request.param
#
# def test_number_is_positive(skaicius):
#     assert skaicius > 0 or skaicius < 0







