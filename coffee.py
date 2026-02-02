cost = 75
payment = 0
valid_coins = [5, 10, 20, 50]

while payment < cost:
    coin = int(input("Give coin (5, 10, 20, 50): ").replace("£", ""))

    if coin in valid_coins:
        payment += coin
        if payment < cost:
            print(f"Amount owed: £{cost - payment}")
    else:
        print("Invalid coin")

change = payment - cost
if change > 0:
    print(f"Change: £{change}")
else:
    print("Amount paid.Thank you!")