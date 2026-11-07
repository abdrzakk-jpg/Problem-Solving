
"""
* move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""
# * SOLVED ! * #

def move_zeros(lst):
    new_list = []
    zeros_num = 0
    for num in lst:
        if(num == 0):
            zeros_num+=1
        else:
            new_list.append(num)
    for _ in range(0, zeros_num):
        new_list.append(0)
    return new_list

test_case=[1, 0, 1, 2, 0, 1, 3]
print(move_zeros(test_case))
