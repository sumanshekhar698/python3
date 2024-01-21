def factorial(n):
	if(n<0):
		print(f'factorial of {n} does not exist')#string formatting while printing
		return
	result =  1
	temp = n
	while(temp>1):
		result*=temp
		temp-=1
	return result



# do the same thing is for loop
print(factorial(-7))
print(factorial(4))