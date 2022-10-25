from math import floor

def numbersplit(num):
    num1 = floor(num / 2)
    num2 = num - num1
    return [num1 , num2]

print(numbersplit(4))
print(numbersplit(10))
print(numbersplit(11))
print(numbersplit(-9))