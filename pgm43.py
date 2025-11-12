#Create class Engine (power) and Wheels (_size). Derive the class Car (model) from Engine & Wheels. Display details of the car using method overriding
class Engine:
    def __init__(self,power):
        self.power=power

    def display(self):
        print(f"Engine Power : {self.power}bhp")

class Wheels:
    def __init__(self,size):
        self._size=size

    def display(self):
        print( f"Wheels : {self._size}")

class Car(Engine,Wheels):
    def __init__(self,power,size,model):
        Engine.__init__(self, power)
        Wheels.__init__(self, size)
        self.model=model

    def display(self):
        super().display()
        Wheels.display(self)
        print(f"Model : {self.model}")

car=Car(80.46,'185/65 R15','Maruti Suzuki Swift')
car.display()
