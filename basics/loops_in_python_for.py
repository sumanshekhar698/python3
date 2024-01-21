def print_even_numbers(end):
	for i in range(end):
	# print(i,end="")
		if (i%2 == 0):
			print(i)

def print_even_numbers(start,end):
	for i in range(start,end):
	# print(i,end="")
		if (i%2 == 0):
			print(i)


def print_steps(start,end,step):
	for i in range(start,end,3):
		print(i)


def print_even_numbers(start,end):
	end+=1
	if(start%2==0):	
		for i in range(start,end,2):#end is excluive
			print(i)
	else:
		start+=1
		for i in range(start,end,2):
			print(i)


def print_even_numbers_optimized(start,end):
	end+=1
	if(start%2!=0):
		start+=1
	for i in range(start,end,2):
		print(i)


# print_even_numbers(10,30)
# print_steps(3,100,4)
# print_even_numbers(3,20)
print_even_numbers_optimized(3,20)
