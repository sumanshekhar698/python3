def power(num1,num2):
	print(num1**num2)

def power_enhanced(num1,num2=1):#default parameters
	print(num1**num2)


# *data can accept 0 or more args and the data will be captured in a tuple
def print_data(*data):# multiple args can be accepted by this fn
	print(data)
	print(type(data))

def print_data(num1,num2,*data):# *data is a way to accept var args in a fn and should be declared at last
	print(num1)
	print(num2)
	print(data)
	print(type(data))



# power(3,5)
power(num2=5,num1=3)# sending the arguuments via parameter variable name
# power_enhanced(2,4)#arguments
# power_enhanced(5)
print_data(8,3,6,7)
print_data(8,8,656,'Simran')