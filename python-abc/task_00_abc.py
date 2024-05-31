#!/usr/bin/env python3
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Dog subclass
class Dog(Animal):
    def sound(self):
        return "Bark"

# Cat subclass
class Cat(Animal):
    def sound(self):
        return "Meow"

# Testing the implementation
bobby = Dog()
garfield = Cat()

print(bobby.sound())  # Output: Bark
print(garfield.sound())  # Output: Meow

# Uncommenting the following lines will raise an error
# animal = Animal()
# print(animal.sound())
