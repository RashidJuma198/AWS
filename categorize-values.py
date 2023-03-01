#Creating a mixed-type list
#Defining a list with different data types
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#using a for loop statement to traverse the list and
# print their data types for each list item

for item in myMixedTypeList:
    print(f"{item} is of the data type {type(item)}")