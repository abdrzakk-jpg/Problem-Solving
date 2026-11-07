
# SOLVED ! #

def xo(s)->bool:
    x_counter = 0
    o_counter = 0
    for i in s.lower():
        if i == 'x':x_counter+=1
        elif i == 'o':o_counter+=1
    return True if x_counter == o_counter else False    