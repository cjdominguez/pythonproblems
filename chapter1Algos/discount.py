"""
Find the Discount

Create a function that takes two arguments:
the original price and the discount percentage as
integers and returns the final price after the discount.

"""
def dis(price, percentage):
    new_p = percentage/ float(100)       #dividing % / 100 moves decimal place to the left
    discount = price - (price * new_p)   # 1000 - (500)
    return round(discount, 2)            # round cuts decimal place @ 2 

print(dis(1000, 50))
