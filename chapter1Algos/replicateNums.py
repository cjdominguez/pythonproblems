def rep_cat(x, y):
    print(str(x)*10 + str(y)*5)

#rep_cat(3,4)


def rep_cat1(x, y):
    new_x = str(x)
    new_y = str(y)
    new_string = new_x*10 + new_y*5
    print(new_string) #must print this first prior to return statement or wont see output 
    return new_string #python doesnt go past the return statement

#rep_cat1(3,4)



def rep_cat(x, y):
    return str(x) * 10 + str(y) * 5


print(rep_cat(3, 4))

