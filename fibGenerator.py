from functools import reduce
"""def fib(limit):
    a,b=0,1

    while a < limit:
        yield a
        a,b=b,a+b
x = fib(5)

for i in fib(5):
    print(i)"""

"""li = [1,3,2,4,5,6,8,7,9]

final_list = list(filter(lambda x:(x%2 != 0),li))
print(final_list)


final_list1 = list(map(lambda x:x*2,li))
print(final_list1)

animals = ['dog', 'cat', 'parrot', 'rabbit']
upper_case = list(map(lambda animal:animal.upper(),animals))
print(upper_case)
"""
"""list1 = [8,5,10,20,50,100]
sum = reduce((lambda x ,y:x+y),list1)
print("Sum =",end=" ")
print(sum)"""

#newlist = [x for x in animals if "a" in x]
#print(newlist)

import pickle
"""cars = ['tata','m&m','jaguar','land rover','audi']
file = "mycar.pkl"
fileobj = open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()"""

file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)
