class Car:  #class 
    def  __init__(self,make,model,year,color):  # constructor runs when you create a new car 
        self.make= make
        self.model = model
        self.year = year
        self.color = color

    def drive(self): #method1
        print("This "+self.model+" car is driving")
    
    def stop(self): #method2
         print("This "+self.model+" is stopped")
