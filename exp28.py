"""Write lambda functions:
(a) To find largest of 2 numbers
(b)  To check the input number is divisible by 5
(c) To remove all strings with length < 5 from a list of strings
(d)  To increment a list of integers by 10% if the number is greater than 1000 else by 5%."""
largest = lambda a,b: a if a>b else b
div = lambda a: "Yes" if not a%5 else "No"
newStrList = lambda List: list(filter(lambda str: len(str) >= 5, List))
increase=lambda a: a+a*.10 if a>1000 else a+a*.05
numlist=[1,2,3,4,5,66,79,1209,1000]

strlist=input("Enter the list of strings:").split(',')
newNumList=[increase(i) for i in numlist]
print(f"Largest among 4 and 8 is {largest(4,8)}"
      f" \n143 is divisible by 5? {div(143)} "
      f"\nStrings with length >=5 : {str(newStrList(strlist)).strip('[]')} "
      f"\nList of numbers : {numlist}"
      f"\nIncreased number list : {str(newNumList).strip('[]')}")
