"""
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z



letter = a
idx = 0
len(letters_arr) = 26

abcdefghijklmnopqrstuvwxyz
z = 25
x = 23 
23 - 13
a = 0
"""
# * SOLVED ! * #

# #hello world

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = lower_case.upper()
def next_13(letter):
    if letter == " ": return
    if letter in lower_case:letters_arr = list(lower_case)
    else:letters_arr = list(upper_case)
    next_ = 0
    for _, itm in enumerate(letters_arr):
        if itm == letter:
            if letters_arr.index(itm) <= 26:  next_ = letters_arr.index(itm) - 13
            else: next_ = letters_arr.index(itm) + 13
            return letters_arr[next_] 
                
                


def rot13(arg:str):
    result = ""
    for word in arg:
        if word == " ":result += " "
        elif word in "1234567890":result += word
        elif word in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""": result += word
        else:result += next_13(word) #type: ignore
    return result   

print(rot13("Abdrzakk"))
print(next_13("z")) 



