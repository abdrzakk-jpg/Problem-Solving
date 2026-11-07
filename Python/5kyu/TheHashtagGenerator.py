
# SOLVED ! #

def generate_hashtag(seq:str):
    if seq:
        new_str = "#"
        for i in seq.split():new_str += i.capitalize()
        if len(new_str) > 140:return False
        else: return new_str
    else:return False