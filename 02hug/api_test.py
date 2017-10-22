#filename: api_test.py
"""test for happy birthday"""
import hug
import api


def tests_happy_birthday():
    response = hug.test.get(api, 'happy_birthday', {
                            'name': 'Timothy', 'age': 25})
    assert response.status == HTTP_200
    assert response.data is not None
