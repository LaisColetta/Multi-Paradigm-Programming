# MPP - Week 5 - OOP Exercises
#Student: Lais Coletta

#Task 5.2: Modify the Student class to extend the Person class which has been modified above. 
#This means the student should send an address to the parent class.
class Person:
    def __init__(self, name, age, addresses):
        self.name = name
        self.age = age
        self.addresses = addresses

    def add_address(self, address):
        self.addresses.append(address)

    def __repr__(self):
        address_str = "\n".join([str(addr) for addr in self.addresses])
        return f'Person("{self.name}", {self.age})\nADDRESS:\n{address_str}'

class Address:
    def __init__(self, house_number, street, town, county, eircode, country="Ireland"):
        self.house_number = house_number
        self.street = street
        self.town = town
        self.county = county
        self.eircode = eircode
        self.country = country

    def __repr__(self):
        return f'{self.house_number} {self.street}, {self.town}, {self.county}, {self.eircode}, {self.country}'

class Student(Person):
    def __init__(self, name, age, college_course, addresses):
        self.name = name
        self.age = age
        self.addresses = addresses
        self.college_course = college_course

    def __repr__(self):
        return f'Student("{self.name}", {self.age}, "{self.college_course}")'

# Create addresses
address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
address2 = Address("5", "Abbey Upper Street", "Forest Place", "Dublin", "D01UY99")

# Create a Person with name, age, and initial addresses
person1 = Person("John", 36, [address1])

# Add more addresses to the person
person1.add_address(address2)

# Create a Student with name, age, college course, and addresses
student1 = Student("Lais", 32, "Data Analysis", [address2])

# Print the representations
print(person1)
print(student1)

