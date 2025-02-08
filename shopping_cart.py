shopping_cart = []
prices = []

print("Welcome to the Shopping Cart program! ")
print()
while True:
  # Menu 
  print("Please Select one of the following:")
  print("1. Add item")
  print("2. View cart")
  print("3. Remove item")
  print("4. Compute total")
  print("5. Edit item")
  print("6. Quit")
  print()
  action = int(input("Please enter an action: "))
  print()

  if action == 1: #Add item
    add_item = input("What item would you like to add? ").capitalize()
    shopping_cart.append(add_item)
    price = float(input(f"What is the price of {add_item}? "))
    prices.append(price)
    print(f"{add_item} has been added to the cart.")
    print()

  elif action == 2: #View cart
    print("The contents of the shopping cart are: ")
    for i in range(len(shopping_cart)):
      number = i + 1 #converts the index to a number
      print(f"{number}. {shopping_cart[i]} - $ {prices[i]:.2f}")
    print()

  elif action == 3: #Remove item
    print("The contents of the shopping cart are: ")
    for i in range(len(shopping_cart)):
      number = i + 1
      print(f"{number}. {shopping_cart[i]} - $ {prices[i]:.2f}")
    print()

    remove_item_number = int(input("Which item would you like to remove? "))
    remove_index = remove_item_number - 1
    if 0 <= remove_index < len(shopping_cart): #checks if the index is valid
      removed_item = shopping_cart.pop(remove_index)
      prices.pop(remove_index)
      print(f"{removed_item} has been removed from the cart.")
    else:
      print("Sorry that is not a valid item number.")
    print()

  elif action == 4: #Compute total
    total_cost = sum(prices)
    print(f"The total price of the items in the shopping cart is: ${total_cost:.2f}")
    print()

  elif action == 5: #Edit item
    print("The contents of the shopping cart are: ")
    for i in range(len(shopping_cart)):
      number = i + 1
      print(f"{number}. {shopping_cart[i]} - $ {prices[i]:.2f}")
    print()

    change_item = int(input("Which item would you like to change? "))
    new_item = input("What is the new item? ").capitalize()
    shopping_cart[change_item - 1] = new_item
    new_price = float(input(f"What is the price of {new_item}? "))
    prices[change_item - 1] = new_price
  elif action == 6: #Quit
    print("Thank you. Goodbye.")
    break
  else:
    print("Sorry, that is not a valid action. Please try again.")
    print()


#Adding an item to the shopping cart
  # print("What item would you like to add? (Type 'quit' to finish): ")
  # add_item = input("Item: ").capitalize()
  # if add_item == "Quit":
  #   break
  # else:
  #   shopping_cart.append(add_item)
  #   price = float(input(f"What is the price of {add_item}? "))
  #   prices.append(price)
  #   print(f"{add_item} has been added to the cart.")

# print()
# print("The contents of the shopping cart are: ")
# for i in range(len(shopping_cart)):
#   number = i + 1
#   print(f"{number}. {shopping_cart[i]} - ${prices[i]}")
#   # print(f"{number}. {shopping_cart} - ${prices}")


  # Removing Items from the shopping cart
# print()
# remove_item_number = int(input("Which item would you like to remove? "))
# remove_index = remove_item_number - 1 #converts the number to an index

# if 0 <= remove_index < len(shopping_cart):
#     removed_item = shopping_cart.pop(remove_index)
#     print(f"{removed_item} has been removed from the cart.")
# else:
#     print("Sorry that is not a valid item number.")

# print()
# print("Updated contents of the shopping cart are: ")
# for i in range(len(shopping_cart)):
#   number = i + 1
#   print(f"{number}. {shopping_cart[i]} - ${prices[i]}")


# Changing an item in the shopping cart
# print()
# change_item = int(input("Which item would you like to change? "))
# new_item = input("What is the new item? ").capitalize()
# shopping_cart[change_item] = new_item
# new_price = float(input(f"What is the price of {new_item}? "))
# prices[change_item] = new_price
# print()


# Updated contents of the shopping cart
# print("Updated contents of the shopping cart are: ")
# for i in range(len(shopping_cart)):
#   number = i + 1
#   print(f"{number}. {shopping_cart[i]} - ${prices[i]}")
# print()


# Compute the total cost of the shopping cart
# total_cost = sum(prices)
# print(f"The total price of the items in the shopping cart is: ${total_cost}")

  