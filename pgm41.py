# Create a class Time with private attributes hour, minute, and second.
# Overload + operator to find the sum of two Time objects.
class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def sum(self,other):
        sec =  self.__seconds  + other.__seconds
        min = self.__minutes + other.__minutes + sec // 60
        hr = self.__hours + other.__hours + min // 60
        sec %= 60
        min %= 60
        return Time(hr, min, sec)

    def __str__(self,other=None):
        if other:
            return self.sum(other)
        else:
            return f"{self.__hours}:{self.__minutes}:{self.__seconds}"

t1=Time(11,35,58)
t2=Time(8,23,12)
print(t1)
print(t2)
print(t1.__str__(t2))