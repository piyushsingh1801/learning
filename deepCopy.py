import copy

list1 = [1,2,[3,4],5,6]

print("Orignal list")
for i in range(0,len(list1)):
    print(list1[i],end=" ")
print("\r")

list2 = copy.deepcopy(list1)

list2[2][0] = 267

print("Orignal list after modifying the copied list2")
for i in range(0,len(list1)):
    print(list1[i],end=" ")
print("\r")

#orignal list remains same before and after making chnages to copied list 

