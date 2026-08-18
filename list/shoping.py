grocery = []
print("")
print("Please enter the items oof the shopping list (type: quit to finish)")

while True:
   item = input("Item: ")
   if item.lower() == "quit":
    break
   else:
     grocery.append(item)
     
print("")
print ("This shopping list is: ")
for i in grocery :
  print (i)

print("")
print ("The shopping list with indexes is: ")
for i in range(len(grocery)):
  print (f"{i}. {grocery[i]}")


item_to_remove = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

for i in range(len(grocery)):
  if item_to_remove == i:
    grocery.pop(i)
    grocery.append(new_item)
    
print ("The shopping list with indexes is: ")
for i in range(len(grocery)):
  print (f"{i}. {grocery[i]}")
 

  

