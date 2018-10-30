class car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
    def display_all(self):
        tax = 0.15
        if self.price < 10000:
            tax = 0.12
        print("Price: " + str(self.price) + "\nSpeed: " + self.speed + 
              "\nFuel: " + self.fuel + "\nMileage: " + self.mileage + "\nTax: " + str(tax) )

car1 = car(2000, "35mph", "Full", "15mpg")
car2 = car(2500, "75mph", "Not Full", "12mpg")
car3 = car(5000, "85mph", "Full", "15mpg")
car4 = car(2000, "100mph", "Half Full", "40mpg")
car5 = car(12000, "80mph", "Full", "35mpg")
car6 = car(13200, "90mph", "Full", "30mpg")

car5.display_all()
