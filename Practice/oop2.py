class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"My name is {self.name},age: {self.age}, and gender: {self.gender}")


myobj=Person("Hiram",25,"Male")
myobj.display()