#Create a class FruitBasket (fruit_name, price per kg).
# Overload '+' operator that adds two fruit baskets with unique fruits having the least price from 2 baskets.
class FruitBasket:
    def __init__(self,fruit_name,price):
        self.fruit_name=fruit_name
        self.price=price

    def __add__(self,other):
        fruits=self.fruit_name +", "+ other.fruit_name
        price=self.price if self.price < other.price else other.price
        return FruitBasket(fruits, price)

    def __str__(self):
        return f"{self.fruit_name} - {self.price}/kg"

f1=FruitBasket("Banana",100)
f2=FruitBasket("Mango",200)
print(f1)
print(f2)
print("Fruits in the basket and price :",f1+f2)