# MPP - Week 5 - OOP Exercises
#Student: Lais Coletta

#Task 5.1: Modify the Person class, from the lecture notes, such that a person can have multiple addresses. You can use a list for this purpose: (Reference: https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/)

# Define a class named "Person" with name, age, and address
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = []  # use a list to store new addresses

# Task 1.2: Add a method (function) to the Person class to add a new address:
    def new_address(self, address):
        self.address.append(address)

    def __repr__(self):
        # Return a string representation of the person, including their name, age, and address
        return f'Person("{self.name}", {self.age})\nADDRESS: {self.address}'

class Address:
    def __init__(self, house_number, street, town, county, eircode, country="Ireland\n"):
        self.house_number = house_number
        self.street = street
        self.town = town
        self.county = county
        self.eircode = eircode
        self.country = country

    def __repr__(self):
        # Return a string representation of the address, including its components
        string = "\n"
        string += f'{self.house_number} {self.street},\n{self.town},\n{self.county},\n{self.eircode},\n{self.country}'
        return string

# Create address 1 details
address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")

# Create address 2 details
address2 = Address("5", "Abbey Upper Street", "Forest Place", "Dublin", "D01UY99")

# Creat person one with name and age
p1 = Person("John", 36, address1)

# Add addresses to the list
p1.new_address(address1)
p1.new_address(address2)

# Print the string representation of the Person instance, which includes name, age, and the address details
print(p1)
