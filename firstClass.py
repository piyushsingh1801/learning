class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.piyush: str
    def myFunc(self):
        self.piyush =  "Hello World!!!!"
        print("Hello my name is "+self.name)
 

    def new_func(self):
        print(self.piyush)

p1 = Person("Piyush" ,21)

p1.myFunc()
p1.new_func()



class Student(Person):
    pass

s1 = Student("Ayush", 23)
print(s1.name)
print(s1.age)
s1.myFunc()