from arrayQFile import ArrayQ

def main():
	choice_num = str(input("Vilken ordning ligger korten i?" ))
	str_list = choice_num.split()
	num_list = [ int(x) for x in str_list ]
	q = ArrayQ()
	for num in num_list:
		q.enqueue(num)
	result = []
	while not q.isEmpty():
		top_card = q.dequeue()
		q.enqueue(top_card)
		next_card = q.dequeue()
		result.append(next_card)
	print (str(result).strip('[]'))

if __name__ == '__main__':
	main()
