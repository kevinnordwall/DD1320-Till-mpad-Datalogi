from linkedQFile import LinkedQ

def main():
	choice_num = str(input("Vilken ordning ligger korten i?" ))
	str_list = choice_num.split()
	num_list = [ int(x) for x in str_list ] # Gör om alla element till integers
	q = LinkedQ() #Skapar en tom kö
	for num in num_list: #Sätter in alla värden i kön
		q.enqueue(num)
	result = []
	while not q.isEmpty(): # Här tar vi bort en och lägger den längst bak i kön, tar nästa i kön och sätter den i result listan, fortsätter tills listan är tom
		top_card = q.dequeue()
		q.enqueue(top_card)
		next_card = q.dequeue()
		result.append(next_card)
	print (str(result).strip('[]'))

if __name__ == '__main__':
	main()
