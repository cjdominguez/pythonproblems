"""

PAPER DOLL: Given a string, return a string where for every character in the original
there are three characters


paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


########################################################################################################

def (string):

    new_string = []
    for x in string:
        new_string.append(x*3)

    return ''.join(new_string)

########################################################################################################

"""


def paper_doll(word):
    new_string = []
    for x in word:
        new_string.append(x * 3)
    return ''.join(new_string)


def paper_dolls(text):
    result = ''
    for char in text:
        result += char * 3
    return result


print(paper_doll("hello"))
print(paper_doll('Mississippi'))