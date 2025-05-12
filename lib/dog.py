#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Unknown",
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Unknown"):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = "Invalid name"
        else:
            self.name = name

        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = "Invalid breed"
        else:
            self.breed = breed

Fido = Dog("", "Beagle")
print(Fido.name)
print(Fido.breed)
