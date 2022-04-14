#Sa en animali xndirna, ete paymany chisht em haskacel :)

class Animal():
  def __init__(self):
    self.name = None
    self.sound = None
    self.makeSound = None

  def set_name(self, n):
      self.name = n

  def get_name(self):
      return self.name

  def set_sound(self):
      self.sound = input("What sound the {} animal makes?".format(self.name))

  def get_sound(self):
      return self.sound

  def make_sound(self):
      self.makeSound = self.sound
      print("The {} animal makes {}".format(self.name, self.makeSound))

animal = Animal()
animal.set_name('Cat')
animal.set_sound()
animal.make_sound()

print('')

#1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
#    Create a function to display the entire attribute and their values in Student class.

class Student():
    def __init__(self, studentId: int, studentName: str, studentClass: int):
        self.studentId = studentId
        self.studentName = studentName
        self.studentClass = studentClass

    def display_info(self):
        print("The {} student's name is {} and he/she studies in {} class".format(self.studentId, self.studentName, self.studentClass))

student = Student(3, "John", 2)

student.display_info()

print('')

#2. Create a Vehicle class without any variables and methods

class Vehicle:
    pass

print('')

#3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle():
    def __init__(self, maxSpeed: int, mileage: int):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

Ferrari = Vehicle(300, 20)

print("Ferrari Max speed is {} and mileage is {}".format(Ferrari.maxSpeed, Ferrari.mileage))

print('')

#4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle():
    def __init__(self, maxSpeed: int, mileage: int):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

class Bus(Vehicle):
    pass

ZhongTong = Bus(80, 130)

print("ZhongTong bus has {} max speed and {} mileage".format(ZhongTong.maxSpeed, ZhongTong.mileage))

print('')

#5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity()
# a default value of 50.

class Vehicle():
    def __init__(self, name: str, maxSpeed: int, mileage: int):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
        self.name = name

    def seating_capacity(self, capacity):
        return "The seating capacity of {} is {}".format(self.name, capacity)

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

cityBus = Bus("Bogdan", 10, 10)
print(cityBus.seating_capacity())






