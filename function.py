# 1. Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying #discount. The function should take the original price (price) and the discount percentage (discount_percent) as #parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    if discount_percent >= 20:
        return price - discount_amount
    else:
        return price
    
finalprice=calculate_discount(150,25)
print(finalprice)


# 2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount   #percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
    
def calculate_discount():
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the percentage dicount of the item: "))
    final_price = price - price * (discount_percent/100)

    if discount_percent != 0:
        print(final_price)

    else:
        print("No discount applied. The final price is: ", price)

calculate_discount()



    

    
     
     
    
    
