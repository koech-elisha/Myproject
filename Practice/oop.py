# class
class Fruits:
    # constructor method
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
    def display(self):
        print(f"I like eating {self.name}, it costs {self.price}, and it is {self.color} in color.")


myobj=Fruits("Orange",50,"orange")
myobj.display()