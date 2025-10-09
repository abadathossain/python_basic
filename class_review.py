# default constructor
class Car:
    def __init__(self):
        self.brand=""
        self.model=""

car1=Car()
car1.brand="Honda"
car1.model="Corolla"
# print(car1.brand,car1.model)


# parameterized construcotr

class Bus:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
bus=Bus("Hyudai","Japan")
print(bus.brand,bus.model)
