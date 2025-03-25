#Create a function named calculate_discount(price, discount_percent) 
#that calculates the final price after applying a discount.
def calculate_discount(price, discount_percent):
    # Apply the discount only if it is 20% or higher
    if discount_percent >= 20:
    #The function should take the original price (price) 
    #and the discount percentage (discount_percent) as parameters.
        return price - (price * discount_percent / 100)
    else:
        #return the original price
        return price

price = float(input("Enter the original price: "))  # Prompt user for the original price
discount_percent = float(input("Enter the discount percentage: "))  # Prompt user for the discount percentage

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price or indicate no discount was applied
if final_price == price:
    print(f"No discount applied. The original price is: {price}")
else:
    print(f"The final price after applying the discount is: {final_price}")


