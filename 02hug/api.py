#filename: api.py
"""A basic (single function) API written using hug"""
import hug


@hug.get('/happy_birthday')
def hello_world(name, age: hug.types.number=1):
    """says happy birthday to a user"""
    return "Happy {age} birthday {name}".format(**locals())
