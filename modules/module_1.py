# In Python Every file is a module
def power(num1,num2):
	print("__name__  ==> ",__name__)
	print(num1**num2)


# Safety Check to prevent Auto Execution
if __name__ == "__main__":
	# print(__name__)
	print("Hey")
	power(5,6)