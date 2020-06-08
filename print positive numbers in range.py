# print positive numbers from range

#taking list input from user
list1 = []
n = input("Enter number of elements: ")

for i in range (0, n):
    ele = input()

    list1.append(ele)
    
print "Input:", list1

#List for positive numbers 
positive_list1 = []

for i in list1:
    if i > 0:
        positive_list1.append(i)

print "Output:", positive_list1

#Taking user input for list
list2 = []

n = input("Enter number of elements: ")

for j in range (0,n):
    ele = input()

    list2.append(ele)
    
print "Input:", list2

#List for positive numbers 
positive_list2 = []

for j in list2:
    if j > 0:
        positive_list2.append(j)

print "Output:", positive_list2
