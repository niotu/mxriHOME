import json


class Device:
    def __init__(self, name, id, state, description=""):
        self.name = name
        self.id = id
        self.is_on = state
        self.is_off = not self.is_on
        self.description = description

    def __str__(self):
        return f'Convector {self.name} id: {self.id} state: {self.is_on}'

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def to_json(self):
        return {self.name: {"id": self.id, "state": self.is_on}}

    def set_description(self, description):
        self.description = description


c = Device("convector", 0, False)
print(c.to_json())
