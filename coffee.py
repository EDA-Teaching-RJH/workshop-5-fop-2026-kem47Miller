#statement of requirements
cost = 75
payment = 0
valid_coins = [5, 10, 20, 50]

while payment < cost:
    try: coin = int(input("Give coin (5, 10, 20, 50): ").replace("£", ""))#try: added
    except ValueError:#added
        print("Invalid Input")#added
        continue#added

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