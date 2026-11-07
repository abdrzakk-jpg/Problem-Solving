
"""
steps

to find 89 
we need to search each number is passed from the equation : 8¹ + 9² = 89

* first: Split the Numbers and return the numbers in array
* second: get the number pos plus 1 [i+1] to avoid muliply with 0 [i * 0 = 0]
* third :   
"""


# SOLVED ! #


def condition_checker(number):
    digits = list(str(number))
    return sum(pow(int(digit), (index+1)) for index,digit in enumerate(digits))

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for i in range(a,b+1):
        if condition_checker(i) == i:result.append(i)
        
    return result

print(sum_dig_pow(155, 1199))