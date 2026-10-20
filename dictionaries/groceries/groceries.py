PRICE = 0

def make_price_dict():
    """Return a dictionary of grocery items.

    Key:   the item name, such as "apple"
    Value: a list with [price_per_unit, unit]
    """
    price_dict = {
        "apple": [0.50, "each"],
        "banana": [0.25, "each"],
        "orange": [0.60, "each"],
        "tomato": [0.40, "each"],
        "onion": [0.35, "each"],
        "potato": [1.80, "kg"],
        "carrot": [1.50, "kg"],
        "rice": [2.20, "kg"],
        "flour": [1.60, "kg"],
        "sugar": [1.40, "kg"],
        "chicken": [6.50, "kg"],
        "beef": [9.80, "kg"],
        "fish": [7.20, "kg"],
        "milk": [1.10, "liter"],
        "cooking oil": [3.25, "liter"],
        "bread": [1.90, "loaf"],
        "eggs": [3.00, "dozen"],
        "butter": [2.75, "pack"],
        "cheese": [4.50, "pack"],
        "salt": [0.80, "pack"],
    }
    return price_dict

def compute_total_cost(item_quantity_list, price_dict):
    total = 0
    for item in item_quantity_list:
        product = item[0]
        quantity = item[1]

        actutal_product = price_dict[product]
        price  = actutal_product[PRICE]

        total += price * quantity 
    return total

def main():
    order = [
        ["apple", 6],
        ["rice", 2],
        ["milk", 3],
        ["eggs", 2],
        ["chicken", 1],
        ["bread", 2],
    ]
    store = make_price_dict()
    budget = float(input("Enter your budget: "))

    total_cost = compute_total_cost(order, store)
    print(f"The total cost for your items are GHS{total_cost:.2f}")
    print("="*50)

    if total_cost < budget:
        margin = budget - total_cost
        print (f"Your order is within budget of GHS{margin:.2f} more!!!")
    elif total_cost > budget:
        margin = total_cost - budget
        print(f"Your order is above budget of GHS{margin:.2f} more!!!")
    else :
        print(f"Your budget and total cost are equal.")

    print("="*50)

if __name__ == "__main__":
    main()
