from array import array

class ArrayQ:

	def __init__(self):
		self.__array = array('i') # Skapar en tom array som vill ha integers

	def enqueue(self, x): # Metod för att lägga till värden
		self.__array.append(x) #Lägger x sist i arrayen

	def dequeue(self): # Metod för att ta bort värden
		pop_value = self.__array.pop(0) #poppar första elementet i arrayen och sparar det i en variabel som vi senare returnerar
		return pop_value

	def isEmpty(self): # Metod för att kolla om arrayen är tom eller inte.
		if self.__array:
			return False
		elif not self.__array:
			return True
