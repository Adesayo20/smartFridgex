from contents import pantry, recipes


def create_shopping_list(data:dict, items:str, amount:int):
    data[item]=data.setdefault(items, 0)+amount

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index+1)] = key
shopping_list= {}
while True:
    print("Please choose a recipe")
    print("----------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
    choice = input(": ")



    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print(f"checking ingredients for {selected_item}")
        print("-------------------------------------")
        ingredients = recipes[selected_item]

        for item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"{item, required_quantity} okay")
            else:
                quantity_to_buy=required_quantity-quantity_in_pantry
                print(f"You don't have enough {item}, you need an additional {quantity_to_buy} gram")
                create_shopping_list(shopping_list, item, quantity_to_buy)
    print()

print("FIND YOUR SHOPPING LIST BELOW")
for grocery in shopping_list.items():
    print(grocery)