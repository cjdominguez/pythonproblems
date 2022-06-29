"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if
 both words begin with same letter


animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False

"""



def animal_cracker(word):
    x = word.split(" ")
    storage = []
    for word in x:
        for letter in range(0,1,1):
            storage.append(word[letter])
    if storage[0] == storage[1]:
        return True
    return False



print(animal_cracker("levelheaded llama"))
print(animal_cracker("levelheaded Liam"))
print(animal_cracker("levelheaded Trust"))
