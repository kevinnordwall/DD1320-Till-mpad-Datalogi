class Pokemon:

	def __init__(self, name, hp, atk, deff, ability1):
		self.name = name
		self.hp = hp
		self.atk = atk
		self.deff = deff
		self.ability1 = ability1

	def __str__(self):
		string = "Name: " + self.name + "\n" + "HP: " + str(self.hp) + "\n" + "Attack: " + str(self.atk) + "\n" + "Defense: " + str(self.deff) + "\n" + "Ability 1: " + self.ability1 + "\n"
		return string

	def PlusAttack(self):
		self.atk = int(self.atk) + 10

	def PlusDefence(self):
		self.deff = int(self.deff) + 10

	def Attack(self):
		print("\n" + self.name + " attackerar med " + self.ability1 + " och skadar " + str(self.atk) + "\n")

def ReadFile():
	fileName = "pokedex.csv"
	pokeList = []
	with open(fileName, encoding = "utf-8") as pokefile:
		firstLine = pokefile.readline()
		for row in pokefile:
			split = row.strip().split(",")
			pokeName = split[2]
			pokeHp = split[3]
			pokeAtk = split[4]
			pokeDeff = split[5]
			pokeAbility1 = split[13]
			pokeObject = Pokemon(pokeName, pokeHp, pokeAtk, pokeDeff, pokeAbility1)
			pokeList.append(pokeObject)
	return pokeList

def Interface():
	pokeList = ReadFile()
	while True:
		searchInput = input("Sök efter en pokemon: ")
		for pokemon in pokeList:
			name = pokemon.name
			if searchInput == name:
				print()
				print(pokemon)
				SubInterface(pokemon)
				break
			else:
				found = False

def SubInterface(pokemon):
	while True:	
		print("1. Höj Attack\n2. Höj Defense\n3. Attackera\n4. Välj ny pokemon\n5. Avsluta programmet")

		try:
			choice = int(input("Vad vill du göra: "))
			if choice == 1:
				pokemon.PlusAttack()
				print("\nNy Attack Power: " + str(pokemon.atk)+ "\n")
			elif choice == 2:
				pokemon.PlusDefence()
				print("\nNy Defense Power: " + str(pokemon.deff) + "\n")
			elif choice == 3:
				pokemon.Attack()
			elif choice == 4:
				print()
				break
			elif choice == 5:
				exit()
		except ValueError:
			print("\nSkriv in en siffra.\n")

if __name__ == '__main__':
	Interface()