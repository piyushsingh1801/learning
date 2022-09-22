class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunc(self):
        print("Hello my name is "+self.name)

p1 = Person("Piyush" ,21)



class Student(Person):
    pass

s1 = Student("Ayush", 23)
print(s1.name)
print(s1.age)
s1.myFunc()