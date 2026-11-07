

# NOT SOLVED #


def temp(*args):
    result = []
    arrays = []
    
    if len(args) == 0: return []
    
    for idx, itm in enumerate(args):
        
        # if item is INT
        if not isinstance(itm, list):
            result.append(itm) 
        else:
            current_item = itm
            if len(current_item) > 1:
                for x in range(len(current_item)-1):
                    result.append(current_item[x])

            
    print(result) 
    
temp(
    1, [2, 3], 4, 5, [6, [7]]
    )
"""
* Input: 1, [2, 3], 4, 5, [6, [7]]
* Output: [1, 2, 3, 4, 5, 6, 7]




"""