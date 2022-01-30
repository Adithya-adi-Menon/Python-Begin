#Functions

def who_am_i():
	name = "adi"
	age  = 30
	print("My name is " + name + "age: "+str(age))
	
who_am_i()

#adding parameters

def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#multiple parameters 
def add(x,y):
	print(x + y)
	
add(7,7)

#Returning Values

def multiply(x,y):
	return x *y
	
print (multiply(7,7))

def square_root(x):
	print(x ** .5)

square_root(64)

def nl():
	print('\n')
nl()
