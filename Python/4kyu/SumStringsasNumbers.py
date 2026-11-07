
# NOT SOLVED YET #
import sys

sys.set_int_max_str_digits(100000000)
def sum_strings(x:str="0", y:str="0") -> str:
    if x == "":
        x_int = 0
    if y == "":
        y_int = 0
        
    if x == "" and y == "":
        x_int = 0
        y_int = 0
    else:
        x_int = int(x)
        y_int = int(y)
        
    return f"{x_int+y_int}"



print(sum_strings("-1", "10"))