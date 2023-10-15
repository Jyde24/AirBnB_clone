import json


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"{self.name} is {self.age} years old, lives at {self.address}"

    def to_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address.__dict__
        }

    @classmethod
    def from_json(cls, data):
        return cls(data["name"], data["age"], Address(**data["address"])


class Address:
    def __init__(self, street, city, code):
        self.street = street
        self.city = city
        self.code = code

    def __str__(self):
        return f"{self.street} {self.city} {self.code}"

    def to_json(self):
        return self.__dict__

    @classmethod
    def from_json(cls, data):
        return cls(**data)


person = Person("Alice", 30, Address("123 Main Street", "Cityville", "13527"))

# Serialize the object to JSON and save it to file
with open("person.json", "w") as file:
    json.dump(person.to_json(), file)

# Reload the object from the JSON file
with open("person.json", "r") as file:
    data = json.load(file)

reload = Person.from_json(data)

print(reload)
