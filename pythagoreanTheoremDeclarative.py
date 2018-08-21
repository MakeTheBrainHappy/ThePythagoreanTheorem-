import math #imports the square root function

def pythagoreanTheorem(a,b): #method to find the third side of the triangle
	c = math.sqrt(a**2 + b**2)
	return c

def main():
	a = 1 #first side
	b = 2 #second side
	print(pythagoreanTheorem(a,b)) #Assuming that you have a right triange, print out the length of the third side. 

main()