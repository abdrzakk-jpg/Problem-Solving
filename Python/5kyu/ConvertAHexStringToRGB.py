

# NOT SOLVED YET #

"""


0:0     ]              ]
1:1     |              | 
2:2     |              |
3:3     |              |
4:4     | decimal      |
5:5     |              |
6:6     |              |
7:7     |              |
8:8     |              | HexaDecimal 
9:9     ]              |
A:10                   |
B:11                   |
C:12                   |
D:13                   |
E:14                   |
F:15                   ]

decimal = 0...9 (10 number)
HexaDecimal = decimal + ABCDEF  (16 char)

RGB use = decimal
HEX use = HexaDecimal


example 1:--------------------
#2EF2E8 

2E = R, (2 * 16^1) + (14*16^0)  =  32+ 14 = 46
F2 = G, (15 * 16^1) + (2 * 16^0) = 240 + 2 = 242
E8 = B, (14 * 16^1) + (8 * 16^0) = 224 + 8 = 232
rgb(46, 242, 232)

example 2:--------------------

#AA22FF

AA = R, (10 * 16^1) + (10 * 16^0) = 160 + 10 = 170
22 = G, (2 * 16^1) + (2 * 16^0) = 32 + 2 = 34
FF = B, (15 * 16^1) + (15 * 16^0) = 240 + 15 = 255

rgb(170, 34, 255)

example 3:--------------------
#Fa3456

FA = R, (15 * 16^1) + (10 * 16^0) = 240 + 10 = 250
34 = G, (3 * 16^1) + (4 * 16^0) = 48 + 4 = 52
56 = B, (5 * 16^1) + (6 * 16^0) = 80 + 6 = 86

rgb(250, 52, 86)

example 3:--------------------
#ffffff
ff = R, (15 * 16^1) + (15 * 16^0) = 240 + 15 = 255
ff = R, (15 * 16^1) + (15 * 16^0) = 240 + 15 = 255
ff = R, (15 * 16^1) + (15 * 16^0) = 240 + 15 = 255
rgb(255,255,255)


"""

# * SOLVED ! *   #

def hex_string_to_RGB(hex_string): 
    hexa_decimal = {
        "0":0,"1":1,"2":2,"3":3,
        "4":4,"5":5,"6":6,"7":7,
        "8":8,"9":9,"A":10,"B":11,
        "C":12,"D":13,"E":14,"F":15
    }
    hex_string = hex_string[1:].upper()
    R = hex_string[0:2]
    G = hex_string[2:4]
    B = hex_string[4:6]
    HEX_red = (hexa_decimal[R[0]] * 16 ** 1 ) + (hexa_decimal[R[1]] * 16 ** 0 )
    HEX_green = (hexa_decimal[G[0]] * 16 ** 1 ) + (hexa_decimal[G[1]] * 16 ** 0 )
    HEX_blue = (hexa_decimal[B[0]] * 16 ** 1 ) + (hexa_decimal[B[1]] * 16 ** 0 )
    
    return {"r":HEX_red, "g":HEX_green, "b":HEX_blue}
    
    
print(hex_string_to_RGB("#FF9933"))