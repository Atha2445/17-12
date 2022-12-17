class Car:
    wheels = 4
    def __init__(self):
        self.company = "TATA"
        self.mileage = 23

car1 = Car()
car2 = Car()

print(car1.mileage)
print(car2.mileage, car1.wheels)