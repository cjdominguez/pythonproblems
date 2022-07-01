"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

########################################################################################################

def function(string = " sentence sentence sentence")

    split(string) into list
    traverse list R to L

    ADDING ELEMNENTS TO NEW LIST

    RETURN new list with .join method
########################################################################################################
"""


def master_yoda(sentence):
    split_sentence = sentence.split(" ")
    yoda_lingo = []

    for x in range(len(split_sentence) -1, -1, -1):
        yoda_lingo.append(split_sentence[x])

    return " ".join(yoda_lingo)


print(master_yoda(sentence="I am home"))


def master_yoda(text):
    return ' '.join(text.split()[::-1])

print(master_yoda("we are ready"))
