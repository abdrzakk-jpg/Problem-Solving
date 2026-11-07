"""
example 1:--------------------
FROM HEX TO RGB
#2EF2E8 

2E = R, (2 * 16^1) + (14*16^0)  =  32 + 14 = 46
F2 = G, (15 * 16^1) + (2 * 16^0) = 240 + 2 = 242
E8 = B, (14 * 16^1) + (8 * 16^0) = 224 + 8 = 232

FROM RGB TO HEX
255 = R, (15 / 16^1) - (15 / 16^0) = 0.9 + 15 = 15,9
255 = G, (15 / 16^1) - (15 / 16^0) = 0.9 + 15 = 15,9
255 = B, (15 / 16^1) - (15 / 16^0) = 0.9 + 15 = 15,9
#fff


ex 1:-----------
rgb(170, 34, 255)
170 = R, (170 / 16) = 10 = A
34 = G, (34 / 16) = 2 =2
255 = B, (255 / 16) = 15 = F


Tests :
method 1:
rgb(148, 0, 211)
R: 148 = (148 / 16) [ 148 / 16^1] = 9 = 9
G: 0 = (0 / 16) = 0 = 0
B: 211 = (211 / 16) = 13 = D
#90D

method 2:

rgb(148, 0, 211)
R: 148 = (148 / 16^1), (148 / 16) = 9..,9..  = 99
G: 0 = (0 / 16^1), (0 / 16) = 0 = 0, 0
B: 211 = (211 / 16^1), (211 / 16) = 
#90D







"""

# * SOLVED * #


def rgb(r, g, b): 
        
    if all(isinstance(x, int) for x in (r,g,b)):
        if r >= 255 :r = 255
        elif r < 0 : r = 0
        if g >= 255 :g = 255
        elif g < 0 : g = 0
        if b >= 255 :b = 255
        elif b < 0 : b = 0
        hexa_decimal = {
            0:"0",1:"1", 2:"2",3:"3",
            4:"4", 5:"5", 6:"6", 7:"7",
            8:"8", 9:"9", 10:"A",11:"B",
            12:"C",13:"D",14:"E",15:"F"
        }
        RED = r // 16
        RED_ = r % 16
        GREEN = g // 16
        GREEN_ = g % 16
        BLUE = b // 16     
        BLUE_ = b % 16
        return f"{hexa_decimal[RED]}{hexa_decimal[RED_]}{hexa_decimal[GREEN]}{hexa_decimal[GREEN_]}{hexa_decimal[BLUE]}{hexa_decimal[BLUE_]}"


print(rgb(148, 0, 211)) # *-> #9400D3 instead #9900DD