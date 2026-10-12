items = [] #list to short items
prices = []

print("Welcome to the shopping Cart Program")

while True :
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    digit = int(input("Please enter an action: "))
    if digit == 1:
        action1 = input("What item would you like add to cart? ")
        items.append(action1)

        price1= float(input(f"What is the price of '{action1}'? "))
        conv_price = float(f"{price1:.2f}")
        prices.append(conv_price)
        print(f"{action1} has been added to the cart.")

    elif digit == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} - GHS{prices[i]}")

    elif digit == 3:
        print("The content of your shoppping cart are: ")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} - GHS{prices[i]}")
        remove_item = int(input("Which item would you like to remove? "))
        for i in range(len(items)):
            if remove_item - 1 == i:
                items.pop(i)
                prices.pop(i)
                print(f"Item removed")
    elif digit == 4:
        total = 0
        for i in prices:
            total += i
        print(f"The total price for all items in the cart is: {total}")
    else:
        break





 