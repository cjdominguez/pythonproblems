"""
 Write a function that stutters a word as if someone is struggling
 to read it. The first two letters are repeated twice
 with an ellipsis ... and space after each, and then
 the word is pronounced with a question mark ?.

"""
"""
def stutter(word):
    stutter_word = word[0:2]
    return(stutter_word + ("...") + stutter_word + ("...") + word)

print(stutter("helloooo"))
"""

def stutter(word):
		return '{0}... {0}... {1}?'.format(word[:2], word)

print(stutter("hello"))
