# class Car:
#     def __init__(self):
#         self.brand=""
#         self.model=""

# car1=Car()
# car1.brand="Honda"
# car1.model="Civic"
# print(car1.model, car1.brand)


class Car:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
    
    def display_info(self):
        print(f"Car brand:{self.brand}\nCar model:{self.model}")

    # def __str__(self):
    #     return f"{self.brand} {self.model}"
car1=Car("Honda","civic")
# print(car1.brand,car1.model)
car1.display_info()
