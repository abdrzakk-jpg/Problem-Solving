
# * SOLVED * #



def parse(data):
    x = 0
    res = []
    for char in data:
        if str(char) == "i":x += 1
        if str(char) == "d":x -= 1
        if str(char) == "s":x **= 2
        if str(char) == "o":res.append(x)
        else:pass
    return res

print(parse("iii"))