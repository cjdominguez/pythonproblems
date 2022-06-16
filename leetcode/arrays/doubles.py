def containsDuplicate(nums):
        #we have an array
        #if there is a double of these elements in there array
        #return true//else false
        #->
        #we have a list (we dont need the index and value just value) of items stored in [nums]
        #check these items
        #iterate through these items
        #we store items we have parsed through in this dictiruionrary
        #if any are the same return true
        #else false


    no_doubles = set()      #does not accept doubles of an element so you cant have 2 number 1's
    for x in nums:
        if x in no_doubles:     #checks if x is in no_doubles set()
            return True
        else:
            no_doubles.add(x)   #adds element to list
    return False


nums = [1,0,2,4,5,6,7,8,9,1]
print(containsDuplicate(nums))
