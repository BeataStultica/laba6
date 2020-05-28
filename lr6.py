from abc import ABC,abstractmethod
class Polygon(ABC):
	def __init__(self,side):
		self.side = side
	@abstractmethod
	def area(self):
		pass
	@abstractmethod
	def volume(self):
		pass

class Tetraedr(Polygon):
	def __init__(self,side):
		super().__init__(side)
	def area(self):
		area = (self.side**2)*(3**(1/2))
		print("\nПлоща тетраєдра зі стороною "+ str(self.side) + ' = ' + str(area))
		return(area)
	def volume(self):
		volume = (2**(1/2)*self.side**3)/12
		print("\nОбєм тетраєдра зі стороною "+ str(self.side) + ' = ' + str(volume))
		return volume


class Dodekaedr(Polygon):
	def __init__(self,side):
		super().__init__(side)
	def area(self):
		area = 3*(self.side**2)*(5*(5 + 2*(5**(1/2))))**(1/2)
		print("\nПлоща додекаєдра зі стороною "+ str(self.side) + ' = ' + str(area))
		return(area)
	def volume(self):
		volume = ((15 + 7*(5**(1/2)))*self.side**3)/4
		print("\nОбєм додекаєдра зі стороною "+ str(self.side) + ' = ' + str(volume))
		return volume
class Ikosaedr(Polygon):
	def __init__(self,side):
		super().__init__(side)
	def area(self):
		area = 5*(self.side**2)*(3**(1/2))
		print("\nПлоща ікосаєдра зі стороною "+ str(self.side) + ' = ' + str(area))
		return(area)
	def volume(self):
		volume = ((3 + 5**(1/2))*5*self.side**3)/12
		print("\nОбєм ікосаєдра зі стороною "+ str(self.side) + ' = ' + str(volume))
		return volume
def main():
	while True:
		fig_type = input("\nВведіть 1 щоб створити тетраєдр, 2 щоб створити додекаєдр або 3 щоб створити ікосаєдр: ")
		side = int(input("\nВведіть довжину сторони: "))
		if fig_type == '1':
			polygon = Tetraedr(side)
		elif fig_type == '2':
			polygon = Dodekaedr(side)
		elif fig_type == '3':
			polygon = Ikosaedr(side)
		polygon.area()
		polygon.volume()
		stop = input("\nПродовжити(y/n): ")
		if stop == 'n':
			break
a = input("Виберіть почати з 1 або 2 частини:")
if a  == '1':
	main()
print("\nЧастина 2")


