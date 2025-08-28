# discount_calculator.py

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount if discount >= 20%.
    
    Args:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage.

    Returns:
        float: Final price after discount, or original price if discount < 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied


def main():
    try:
        # Prompt user for inputs
        original_price = float(input("Enter the original price of the item: "))
        discount = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount)

        if discount >= 20:
            print(f"\n✅ Discount applied! Final price: ${final_price:.2f}")
        else:
            print(f"\nℹ️ No discount applied. Price: ${original_price:.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
