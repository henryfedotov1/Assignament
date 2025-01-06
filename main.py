#1
def Hiyuvi_Shalem(lst):
    for num in lst:
        if num < 0:
            raise ValueError("The number should be a positive number!")
        elif num % 2 != 0:
            raise ValueError("The number is not an even number!")


#2
def rem(num):
    return num % 2 == 0

def Filter2(lst):
    return list(filter(rem, lst))


lst = [2, 4, 6, 8, 9]
result = Filter2(lst)
print(result)


#3
import functools
def add(x, y):
    return int(x) + int(y)

def sum_of_digits(number):
    result = functools.reduce(add, str(number))
    return result

print(sum_of_digits(104))
