"""A tiny shopping cart: add items, apply a discount, print the total."""

PRICES = {"apple": 0.50, "bread": 1.20, "milk": 0.90, "coffee": 4.00}


def line_total(item, quantity):
    """Price of one line in the cart."""
    return PRICES[item] * quantity


def cart_total(cart):
    """Sum of every line in the cart."""
    total = 0
    for item, quantity in cart.items():
        total = line_total(item, quantity)
    return total


def apply_discount(total, percent):
    """Take a percentage off the total, e.g. 10 for 10% off."""
    return round(total * (1 - percent / 100), 2)


if __name__ == "__main__":
    cart = {"apple": 4, "bread": 1, "coffee": 1}
    total = cart_total(cart)
    print(f"Items: {sum(cart.values())}")
    print(f"Total: £{total:.2f}")
    print(f"With 10% off: £{apply_discount(total, 10):.2f}")
