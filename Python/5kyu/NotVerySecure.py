"""
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore


example-1|------------
input:"hello world_"
output: False (there is `_`)

example-2|------------
input: "PassW0rd"
output: True (char & digit)


"""

#* Solved *#



def alphanumeric(password: str = "") -> bool:
    striped_pwd = password.strip()
    if len(striped_pwd) == 0: return False
    bool_map = [
        [ # not allowed (unprintble + symboles)
        *list(range(0, 48)), 
        *list(range(58, 65)) , # [*] for unpack: [[],[], [],[]] => [,,,,,]
        *list(range(91, 97)), 
        *list(range(123, 256))
        ]
    ]

    for i in striped_pwd:
        if ord(i) in bool_map[0]:
            return False
    return True


# i w'll use the `boolean map theory`
# its depends on the fields that is allowed by the ASCII Chars like: 
# field from 91-...-96 is not allowed (contains [ / ^ _ `)
# field from 48-...-57 is allowed (containds digits 0-9 )