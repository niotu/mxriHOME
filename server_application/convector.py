import json


class Convector:
    def __init__(self, name, id, state):
        self.id = id
        self.name = name
        self.is_on = state
        self.is_off = not self.is_on

    def __str__(self):
        return f'Convector {self.name} id: {self.id} state: {self.is_on}'

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def to_json(self):
        return {self.name: {"id": self.id, "state": self.is_on}}


c = Convector("convector", 0, False)
print(c.to_json())
