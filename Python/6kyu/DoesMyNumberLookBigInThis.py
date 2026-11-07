
# * SOLVED * #
def narcissistic( value ):
    result = 0
    for v in str(value):
        result += pow(int(v), len(str(value)))
    return result == value
        
        
print(narcissistic(1))