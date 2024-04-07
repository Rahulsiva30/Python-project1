foods = []
prices = []
total = 0


while True:
    food = input("Enter the food item (e to exit):")
    if food.lower() == "e":
        break
    else:
        price = float(input(f"enter the {food} price $:"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"your total price is ${total}")