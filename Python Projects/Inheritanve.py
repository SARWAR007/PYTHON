class Father:

    __car = "Ferrari"
    __house = "Villa"
    __bank_balance = "40 billion USD"


    def business(self):

        print("Chai business")


    def to_marry(self):

        print("Preeti")


    def __get_Car(self):
        

        return "Vilal"
        print(self.car)

class Son(Father):

    def to_marry(self):

        print("Kreeti")

#print("Huse is:",Father.house)
       
obj1 = Father()
print(obj1.__Father__get_Car())

obj1.to_marry()

print("Huse is:",Son.house)

obj = Son()

obj.to_marry()


