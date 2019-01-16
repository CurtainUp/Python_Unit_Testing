# In the test class' setUpClass() method, create an instance of Animal and Dog (Be sure to pass in a name argument). Write test cases to verify the I/O of the following methods of Animal and Dog.

import unittest
import sys
sys.path.append('../')
from animal import Animal
from animal import Dog

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.bob = Dog("Bob")
    cls.steve = Animal("Steve")

  def test_animal_creation(self):
    murph = Dog("Murph")
    self.assertIsInstance(murph, Dog)

# Animal object has the correct name property.
  def test_dog_has_name(self):
    result = self.bob.get_name()
    expected = "Bob"
    self.assertEqual(result, expected)

# Set a species and verify that the object property of species has the correct value.
  def test_can_set_species(self):
    self.assertEqual(self.bob.get_species(), "Dog")
    self.bob.set_species("canine")
    self.assertEqual(self.bob.get_species(), "canine")

# Invoking the walk() method sets the correct speed on the both objects.

  def test_animal_walking_legless(self):
    animal = Animal()
    with self.assertRaises(ValueError):
      animal.walk()

  def test_animal_walking(self):
      animal = Animal()
      animal.set_legs(12)
      animal.walk()
      expected = 1.2
      result = round(animal.speed, 1)
      self.assertEqual(result, expected)

  def test_dog_walking(self):
    self.bob.set_legs(4)
    self.bob.speed = 2
    self.bob.walk()
    result = self.bob.speed
    expected = 2.8
    self.assertEqual(result, expected)

# The animal object is an instance of Animal.
  def test_animal_obj_is_instance(self):
    self.assertIsInstance(self.steve, Animal)

# The dog object is an instance of Dog.
  def test_dog_obj_is_instance(self):
      self.assertIsInstance(self.bob, Dog)

if __name__ == '__main__':
  unittest.main()