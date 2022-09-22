import copy

list1 = [1,2,[3,4],5,6]

print("Orignal list1")
for i in range(0,len(list1)):
    print(list1[i],end=" ")

print("\r")
#shallow copying
list2 = copy.copy(list1)
#making changes in copied list
list2[2][1] = 45
#orignal list after making changes in copied list2
print("Orignal list1")
for i in range(0,len(list1)):
    print(list1[i],end=" ")

print("\r")

#In shallow copy making changes in copied object reflects in orignal object 