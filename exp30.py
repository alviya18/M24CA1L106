"""Write recursive functions to
(a) find the factorial of a number
(b) find the nth Fibonacci number
(c) find the sum of an integer list
(d) find the sum of first N whole numbers
(e) reverse a string."""
def factorial(num):
    if num<=1:
        return 1
    return num * factorial(num - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def sumOfList(list):
    if len(list) == 0:
        return 0
    return list[0] + sumOfList(list[1:])

def numberSum(a):
    return a-1 + numberSum(a-1) if a >= 1 else 0

def stringReverse(string):
    if string == "":
        return ""
    return string[-1] + stringReverse(string[:-1])

print(f"7! is {factorial(7)}"
      f"\nThe 10th number in fibonacci series is {fibonacci(10)}"
      f"\nSum of the list 1,45,48,74,2,24,9 is {sumOfList([1,45,48,74,2,24,9])} "
      f"\nSum of first 45 whole numbers is {numberSum(45)}"
      f"\nHello word reversed is {stringReverse('hello world')}")

