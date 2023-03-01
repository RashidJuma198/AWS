myString = "This is a string"

print(myString)

#getting the data type

print(type(myString))

#Converting the return value to string use str() function

print(myString + " is of data type "+ str(type(myString)))

#String Concatination

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Working with input strings

name = input("what is your name? ")
print(name)

#formatting output strings

color = input("what is your favorite color? ")
animal = input("what is your favorite animal? ")

print("{}, you like a {} {}!".format(name,color,animal))