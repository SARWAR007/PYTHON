class Students:

    studentcounter = 0

    counter = 0

    fee = 15000

    #discountedfee = 0

    def __init__(self,age,name,rollno,course):

        print("Inside constructor")


        self.name = name
        self.age = age

        self.rollno = rollno
        self.course = course

        Students.studentcounter += 1

        print("Counter is",Students.studentcounter)

    def print_info(self):

        print("Inside object function")

        print(self.name)

        print(self.age)

        print(self.rollno)

        print(self.course)

        Students.counter += 1

        print("Counter inside function print_info is",Students.counter)

    @classmethod
    def discount(cls,percentage):
        discounted_fee = 0
        print("Fees is :",cls.fee)

        if (percentage >= 80):

            print("Inside if")

            discounted_fee =  cls.fee*(percentage/100)
            #=print("The discounted fee is :", discounted_fee)


            print("The discounted fee is :", discounted_fee)

        print("Class is :",cls)



print("Before")
obj = Students(25,"ROhit",1,"Python")

print("After")

print("Age is :", obj.age)

print("Name is :", obj.name)

print("Roll no is :",obj.rollno)

print("Course is :",obj.course)


obj2 = Students(32,"Virat",2,"C++")

print("Age is :", obj2.age)

print("Name is :", obj2.name)

print("Roll no is :",obj2.rollno)

print("Course is :",obj2.course)

obj3 = Students(None,None,None,None)

print("Age is :", obj3.age)

print("Name is :", obj3.name)

print("Roll no is :",obj3.rollno)

print("Course is :",obj3.course)



print(obj2.print_info())

print(dir(obj2))
Students.discount(80)
