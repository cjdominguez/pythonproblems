"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald

Note: 'macdonald'.capitalize() returns 'Macdonald'
########################################################################################################
input: macdonald

funtion(input):



input.lower() # lowers input incase something else is capitalized

traverse the string L --> R using RANGE
    @ 0 and 3 index (1st and 4th letters).upper() # M & D letter

#break out of loop

return string

########################################################################################################

"""


def old_mcdonald(name):

    new_name = list(name)
    for letter in range(0, 4, 3):
        new_name[letter] = (new_name[letter].upper())
    return "".join(new_name)

print(old_mcdonald("macdonald"))


