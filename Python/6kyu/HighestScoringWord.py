


# * SOLVED * #

def high(x: str):
    scores_container = []
    alphabet = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
        "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
        "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
        "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
        "z": 26
    }
    x_parts = [word for word in x.split()]
    
    for _, word in enumerate(x_parts): # -> [(0, "aa"), (1, "b")]
        scores_container.append((sum([alphabet[i] for i in word]), word))
        
    scores_container.sort(key=lambda x: x[0])
    if len(scores_container) == 2:
        if scores_container[0][0] == scores_container[1][0]:
            return scores_container[0][1]
    return scores_container[-1][1]
    
    
    
print(high("qxsospkps ghozsuxr imdpnfhwg cbxxcavxa gvng ezesg hwvprurto ctezu rxaotkpp jflh qmszkcqa swadphaokm emipxnvu grptujtaun dnyhwlzssi qwrfnsvzoa zvspmva rsahwbyhjy dhaymlxs vbaova riliifeslo shlr djwwj sroqn dxsosh"))

    
    