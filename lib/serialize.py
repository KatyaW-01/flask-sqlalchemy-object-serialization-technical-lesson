# lib/serialize.py

from pprint import pprint
from marshmallow import Schema, fields

# model

class Dog:
    def __init__(self, name, breed, tail_wagging = False):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging

    def give_treat(self):
        self.tail_wagging = True

    def scold(self):
        self.tail_wagging = False

#schema
class DogSchema(Schema):
    name = fields.String()
    breed = fields.String()
    tail_wagging = fields.Boolean()

# create model instance and schema instance
dog = Dog(name="Snuggles", breed="Beagle", tail_wagging=True)

dog_schema = DogSchema()
#dump and dumps
dog_dict = dog_schema.dump(dog)
pprint(dog_dict)

dog_json = dog_schema.dumps(dog)
pprint(dog_json)

#filtering
dog_summary_only = DogSchema(only=("name","breed")).dumps(dog)
pprint(dog_summary_only)

dog_summary_excludes = DogSchema(exclude=("tail_wagging", )).dumps(dog)
pprint(dog_summary_excludes)

#Serialize a collection
dogs = [Dog(name="Snuggles", breed="Beagle", tail_wagging=True),
        Dog(name="Wags", breed = "Collie", tail_wagging=False)]
dictionary_list = DogSchema(many=True).dump(dogs)
pprint(dictionary_list)
json_array = DogSchema(many=True).dumps(dogs)
pprint(json_array)