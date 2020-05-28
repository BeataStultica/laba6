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

#Частина 2
class Police:
	def spravka_syd(self,person):
		return("Cправка про судимість на імя " + person.surname)
	def search_p(self,person):
		if person.pasport:
			return False
		return True

class Bank:
	def __init__(self, persent):
		self.persent = persent
		self.pay = 100
	def straf(self,person):
		return("Квитанція про сплату штрафа на імя " + person.surname + " на суму " + str(int(self.pay*(1+self.persent/100))))
	def pay_kom(self,person):
		return("Квитанція про оплату комунальних послуг за адресою " + person.mesto_jitel)

class Zvit:
	def __init__(self):
		self.collection = []
	def update_z(self,posluga):
		self.collection.append(posluga)
class Pasport_Table:
	def __init__(self):
		self.zvit = Zvit()
		self.bank = Bank(10)
		self.get_pasport_coin = 0
		self.zagr_pasport_coin = 0
		self.pereof_coin = 0
		self.vyp_coin = 0
		self.prop_coin = 0

	def get_pasport(self,person):
		svid_pro_narod = person.get_svid()
		kv = ''
		if person.age > 18 and person.pasport == None:
			print("\nОплатіть штраф за просрочку\n")
			kv = self.bank.straf(person)
		print("\nВидано паспорт на імя " + svid_pro_narod[1] + ' '+ svid_pro_narod[2])
		self.get_pasport_coin += 1
		person.pasport = [person.surname, person.mesto_jitel, "Паспорт"]
		self.zvit.update_z(["Видано паспорт на імя " + svid_pro_narod[1] + ' '+ svid_pro_narod[2], person.get_foto(), jek.get_spravka(person.surname), svid_pro_narod,kv])
	
	def get_zagr_pasport(self,person):
		svid_pro_narod = person.get_svid()
		sp_voen = ''
		if person.age < 27:
			sp_voen = v.voen_spravka(person)
		if not person.pasport:
			print("\nВідсутній паспорт\n")
			self.get_pasport(person)
		sp_sud = police.spravka_syd(person)
		print("\nВидано закордонний паспорт на імя " + svid_pro_narod[1] + ' '+ svid_pro_narod[2])
		self.zagr_pasport_coin += 1
		person.zagr_pasport = [person.surname, person.mesto_jitel, "Закордонний паспорт"]
		self.zvit.update_z(["Видано закордонний паспорт на імя " + svid_pro_narod[1] + ' '+ svid_pro_narod[2], person.get_foto(),person.pasport , sp_sud, sp_voen])
	def info(self):
		print("\nЗвіти про роботу паспортного стола")
		print("\nВидано паспортів:" + str(self.get_pasport_coin))
		print("\nВидано закордонних паспортів:" + str(self.zagr_pasport_coin))
		print("\nПереоформлено паспортів: " +str(self.pereof_coin))
		print("\nВиписано з місця проживання: " +str(self.vyp_coin))
		print("\nПрописано на нове місце проживання: " + str(self.prop_coin)+'\n')
		for i in self.zvit.collection:
			print(i)
	def remake_pasport(self,person):
		pr = input("Причина переоформлення: 1 - втрата, 2 - вкрадено")
		straf = ''
		if pr == '1':
			straf = self.bank.straf(person)
		elif pr == '2':
			s = police.search_p(person)
			if not s:
				straf = self.bank.straf(person)
		self.pereof_coin += 1
		za = person.get_zayava(pr)
		print("\nУспішно переоформлено\n")
		person.pasport = [person.surname, person.mesto_jitel,"Паспорт"]
		self.zvit.update_z(["Переоформлено паспорт на імя "+person.surname +' ' + straf, person.get_zayava(pr)])
	def vipiska(self,person):
		print("\nУспішно виселено\n")
		self.zvit.update_z(["Виписка з місця проживання " +person.surname, self.bank.pay_kom(person), person.get_zay_vyp(), str(person.pasport)])
		person.mesto_jitel = None
		person.pasport[1] = None
		self.vyp_coin +=1
	def propiska(self,person, new_adres):
		if person.pasport[1] != None:
			print("Виселіться спочатку з поточного місця проживання")
		else:
			print("\nУспішно заселено\n")
			person.mesto_jitel = new_adres
			person.pasport[1] = new_adres
			self.prop_coin += 1
			self.zvit.update_z(["Прописка на нове місце проживання " +person.surname + 'за адресою '+new_adres, jek.get_spravka_prop(person),person.get_zay_pos(new_adres), str(person.pasport)])
	def template(self):
		self.get_pasport()
		self.get_zagran_pasport()
		self.reg_new_prop()
		self.update_pasport()
class Voenkomat:
	def voen_spravka(self,person):
		return("Справка з воєнкомата на імя " + person.surname)

class Gromadanin:
	def __init__(self,age,name,surname,mesto_jitel,pasport = None):
		self.age = age
		self.name = name
		self.surname = surname
		self.mesto_jitel = mesto_jitel
		self.pasport = pasport
		self.zagr_pasport = None
	def get_svid(self):
		return(["Свідоцтво про народження ", self.name, self.surname, self.age])
	def get_foto(self):
		return(self.surname + '.jpg')
	def get_zay_vyp(self):
		return("Я " + self.surname+" прошу виселити мене з мого нинішнього місця проживання " + self.mesto_jitel)
	def get_zay_pos(self, new_jitel):
		return("Я " + self.surname+" прошу поселити мене за адресою " + new_jitel)
	def get_zayava(self, pr):
		if pr == '1':
			pr = "втрати"
		elif pr == '2':
			pr = 'крадіжки'
		return("Я " + self.surname+" прошу видати мені новий паспорт по причині " + pr)

class JEK:
	def get_spravka(self, surname):
		return('Справка про оплату ' + surname)
	def get_spravka_prop(self,person):
		return("Справка про дозвіл на зміну місця прописки")

v = Voenkomat()
pt = Pasport_Table()
police = Police()
jek = JEK()

while True:
	new_g = input("\nСтворити нового громадянина?(y/n)")
	if new_g == 'n':
		pt.info()
		break
	age = int(input("\nВведіть його вік: "))
	name = input("\nВведіть його імя: ")
	surname = input("\nВведіть його прізвище: ")
	place = input("\nВведіть його місце проживання: ")
	grom =  Gromadanin(age,name,surname,place)
	while True:
		f = input("\nВиберіть що зробити в паспортному столі(1 - оформити паспорт, 2 - переоформити паспорт, 3- оформити закордонний паспор, 4 - виписатися, 5 - прописатися, решта - створити нового громадянина): ")
		if f == '1':
			pt.get_pasport(grom)
		elif f == '2':
			pt.remake_pasport(grom)
		elif f == '3':
			pt.get_zagr_pasport(grom)
		elif f == '4':
			pt.vipiska(grom)
		elif f == '5':
			new_ad = input("Введіть нову адресу проживання: ")
			pt.propiska(grom,new_ad)
		else:
			break
