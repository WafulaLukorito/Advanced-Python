
# *Python comes with a built-in json module that can be used to work with JSON data. It can encode and decode JSON data.

# *The json module has two methods dumps and loads. The dumps method is used to convert a Python object into a JSON string. The loads method is used to convert a JSON string into a Python object.

# *Import the json module:

from json import JSONEncoder
import json

# * Serializing/encoding... Take python dictionary and convert it to JSON

person = {'name': 'Bob', 'languages': [
    'English', 'Fench'], 'married': True, 'age': 32}

# * Convert into JSON string
# Can also use separators=(',', ': ')
# person_json = json.dumps(person, indent=4, sort_keys=True)
# print(person_json)

# * Convert into JSON string and write to file

# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)


# * Deserializing/decoding... Take JSON and convert it to python dictionary

person_json2 = '{"name": "Benedict", "languages": ["English", "French"], "married": true, "age": 32, "children": null}'
# * Convert JSON string into Python object

person2 = json.loads(person_json2)
# print(person2)

# * Convert JSON string from file into Python object

with open('example.json', 'r') as file:
    person3 = json.load(file)
    # print(person3)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)

# * Create custom encoder function


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


# * Convert into JSON string
user_json = json.dumps(user, default=encode_user)
print(user_json)


# * Inbuilt JSON encoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


user_json2 = json.dumps(user, cls=UserEncoder)
print(user_json2)

# * Decode using custom decoder function

# Create custom decoder function


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(user_json, object_hook=decode_user)
print(type(user))
print(user.name)
