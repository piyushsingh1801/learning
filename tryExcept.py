x = 10
try:
    print(x/0)
except:
    print("math error")

try:
    print(y)
except:
    print("y is not defined")
else:
    print("nothing went wrong")

try:
    print("hello")
except:
    print("some error occured")
else:
    print("nothing went wrong")

try:
    print("hello")
except:
    print("some error occured")
finally:
    print("try and except blocks are done")