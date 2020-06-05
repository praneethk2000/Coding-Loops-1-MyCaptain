#Coding functions

#Assigning elements to different lists
list1 = [2, 4, 6, 8, 10, 12]
print list1

list2 = [1, 3, 5, 7, 9, 11]
print list2

list1.append(14)
print list1

list2.append(13)
print list2


#Accessing elements from a tuple
myTuple = ("AI", "ML", "DL")
print myTuple

print myTuple[0]

#Removing different dictionary elements
myDict = {
    "Apple" : "Red",
    "Mango" : "Yellow",
    "Grapes" :"Green"
    }

print myDict

del myDict["Grapes"]
print myDict
