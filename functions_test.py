#This are set of instructions that are use to perform specific task.
#We use def keyword to define a function in python
#A function can take in parameter or not
#Example :Calculating the area of a rectangle using function

# def maureen(name):
#     for x in range(1,6):
#         print(name)
    

# maureen("Rashid")

# a = 7
# b = 9
# c= a+b
# print(c)

# def sum(a,b):
#     c = a+b
#     return c

# def multiply(a,b):
#     return a*b

# num1 = int(input("Enter first Value: "))
# num2 = int(input("Enter second Value: "))

# results = multiply(num1,num2)

# print("The multiplication of the two values is "+ str(results))



myfile = open("carol.txt","a")
content = myfile.write("I love you so much")
print(content)
myfile.close()
