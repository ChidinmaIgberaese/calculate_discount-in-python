def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount and the final price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the final price
if final_price == price:
    print(f"No discount applied. The original price is: ${price:.2f}")
else:
    print(f"After applying the discount, the final price is: ${final_price:.2f}")
