def calculate_cart_total(*prices):
    """Calculate total for any number of item
    Parameters: Variable number of price values
    returns: Total sum of all pruves rounded to two decimals
    """
    # Check if cart is empty
    if not prices:
        return 0.00
    # sum of all prices
    subtotal = sum(prices)
    return round(subtotal, 2)
print(f"Empty Cart: ${calculate_cart_total()}")
print(f"1 item Cart: ${calculate_cart_total()}")
print(f"2 items Cart: ${calculate_cart_total()}")
print(f"3 items Cart: ${calculate_cart_total()}")

def create_order(customer_name, **items):
    """Create an order with any menu items"""
    order = {
        "customer": customer_name,
        "items": items,
        "item_count": len(items)
    }
    return order

# DIfferent customers, different orders
order1 = create_order("Alex, pizza = 2,soda = 56, wings = 67")