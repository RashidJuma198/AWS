#Definining the list in python
myFruitList = ["apple","banana","cherry"]
print(myFruitList)

print(type(myFruitList))

#accessing the list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#Changing the values in a list

myFruitList[2] = "orange"
print(myFruitList)

#Introducing Tuple 
#Tuple is like a list but its values cannot be change
myFinalAnswerTuple = ("apple","banana","pineapple")
print(myFinalAnswerTuple)


#accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Introducing the dictionary Data type
#A dictionary is a list with named positions (keys).
myFavoriteFruitDictionary = {
    "Akua": "apple",
    "Saanvi": "banana",
    "Paulo": "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Accessing Dictinary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Paulo"])
print(myFavoriteFruitDictionary["Saanvi"])