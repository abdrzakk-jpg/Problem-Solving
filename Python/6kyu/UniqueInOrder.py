
# * SOLVED ! * #

def unique_in_order(sequence):
    items_arr = list(sequence)	
    for i in range(len(items_arr)):
        for _ in range(len(items_arr)//2):
            if i+1 >= len(items_arr):break
            else:
                if items_arr[i] == items_arr[i+1]: items_arr.pop(i+1)
    return items_arr


print(unique_in_order("1234567789907"))