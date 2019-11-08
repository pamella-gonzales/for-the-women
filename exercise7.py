# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

class Car:
	
	def __init__(self, year=0, make="", model=""):
		self.year = year
		self.make = make
		self.model = model

	def age(self, str):
		return(2019 - year)
    
	mycar = Car(2011,"Benz", "bugeye")
	print(mycar)
	print(mycar.age)


		

