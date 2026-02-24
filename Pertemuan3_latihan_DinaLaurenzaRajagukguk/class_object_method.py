#CLASS
#create class
class MyClass:
  x = 5
#create object
p1 = MyClass()
print(p1.x)
#delete objects
del p1
#multiple objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)
#the pass statement
class Person:
  pass
#init
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
#self
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil", 25)
p1.greet()

#class properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)

#access properties
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
car1 = Car("Toyota", "Corolla")
print(car1.brand)
print(car1.model)

#modify properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Tobias", 25)
print(p1.age)
p1.age = 26
print(p1.age)

#delete properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Linus", 30)
del p1.age
print(p1.name) # This works
# print(p1.age) # This would cause an error

#class method
class Person:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()

#methods with parameters
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))