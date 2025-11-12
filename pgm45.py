#Create class Currency (amount, unit). Overload the '==' operator to determine if 2 currencies are equal.
class Currency:
    def __init__(self,amount,unit):
        self.amount = amount
        self.unit = unit

    def __eq__(self,other):
        return self.amount == other.amount and self.unit == other.unit

currency1 = Currency("1500","USD")
currency2 = Currency("1500","USD")
print(currency1.unit," ",currency1.amount)
print(currency2.unit," ",currency2.amount)
if currency1 == currency2:
    print("Currency equal")
else:
    print("Currency unequal")