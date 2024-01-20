def factorial(n):
	if(n<0):
		print(f'factorial of {n} does not exist')
		return
	result =  1
	temp = n
	while(temp>1):
		result*=temp
		temp-=1
	return result




print(factorial(-7))
print(factorial(4))