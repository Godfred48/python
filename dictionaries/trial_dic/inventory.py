"""a shop inventory using nested dictionaries (a dictionary inside a dictionary), with functions."""

inventory = {
    "apple":  {"price": 2.5,  "quantity": 10, "category": "fruit"},
    "milk":   {"price": 8.0,  "quantity": 4,  "category": "dairy"},
    "bread":  {"price": 5.0,  "quantity": 0,  "category": "bakery"},
    "banana": {"price": 1.5,  "quantity": 25, "category": "fruit"},
    "cheese": {"price": 12.0, "quantity": 6,  "category": "dairy"},
}

#function for total value 
def get_total_value(inv):
    total = 0
    for key, value in inv.items():# loop through each value and get details from dict
        price = value["price"]
        quantity = value["quantity"]
        total += price * quantity
    return total

#function for get out of stock
def get_out_of_stock(inv):
    out_of_stock = []
    for key, value in inv.items():
        name = key
        details = value
        quantity = details["quantity"]
        if quantity == 0:
            out_of_stock.append(name)
    return out_of_stock

#group categories 
def group_by_category(inv):
    groups = {}
    for key, value in inv.items():
        category = value["category"]
        if category not in groups:
            groups[category] = []  # create an empty list
        groups[category].append(key)
    return groups

#function for restock 
def restock(inv, item, amount) :
        if item not in inv:
            return False
        else: 
           inv[item]["quantity"] += amount #update quantity
        
        return True

#unction for sell item 
def sell_item(inv, item, amount):
    if item not in inv:
        return False 
    elif inv[item]["quantity"] < amount :
        return False
    else :
        inv[item]["quantity"] -= amount 
    return True

#function get_most_valuable(inventory)
def get_most_valuable(inv):
    best_item = None
    best_value = 0

    for key, value in inv.items():
        price = inv[key]["price"]
        quantity = inv[key]["quantity"]
        stock_value = price * quantity

        if stock_value > best_value:
            best_value = stock_value
            best_item = key

    return best_item , best_value

def main():
    print("Total inventory value:", get_total_value(inventory))
    print("Out of stock:", get_out_of_stock(inventory))
    print("By category:", group_by_category(inventory))
    print("Restock bread:", restock(inventory, "bread", 12))
    print("Restock eggs:", restock(inventory, "eggs", 5))
    print("Sell 3 milk:", sell_item(inventory, "milk", 3))
    print("Sell 5 milk:", sell_item(inventory, "milk", 5))
    print("New total value:", get_total_value(inventory))
    print("Out of stock:", get_out_of_stock(inventory))
    name, value = get_most_valuable(inventory)
    print(f"Most valuable item: {name} ({value})")


if __name__ == "__main__":
    main()