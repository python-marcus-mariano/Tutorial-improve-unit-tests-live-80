"""
Inprove unit tests with Faker

Tutorial-improve-unit-tests-live-80

Homepage and documentation:


License: GNU GENERAL PUBLIC LICENSE Version 3

"""

from faker import Faker

faker = Faker('pt_BR')

d = {
    'name': faker.name()
}

# Explore faker instance

print(d)
