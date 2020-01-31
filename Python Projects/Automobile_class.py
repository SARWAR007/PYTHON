class Automobile:

    Price = 500000

    def __init__(self,model,engine,mfddate):

        print("Constructor vehicle")

        self.model = model
        self.engine = engine
        self.mfddate = mfddate

    def car_info(self):

        print("Vehicle Details :")
        print("-------------------")
        print("\n")

        print("Model of the car is :",self.model)

        print("Engine is:",self.engine)


        print("Mfddate is :",self.mfddate)


    @staticmethod
    def flagship(Price):

        class_range = ''

        if (Price > 150000) and (Price < 300000):

            class_range = 'Cheap range'

            print("The flagship car is ",class_range)

        elif (Price > 300000) and (Price < 1000000):

            class_range = 'SUV'

            print("The flagship car is ",class_range)

        elif (cls.Price > 1000000):

            class_range = 'Premium'

            print("The flagship car is ",class_range)



obj = Automobile('XR32','7000Hp','2016')

print(obj.car_info())

Automobile.flagship(500000)



            



        


    
