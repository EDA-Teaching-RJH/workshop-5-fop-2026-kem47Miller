#statement of requirements
DRINKS = {
    "coffee": 75,
    "tea": 50,
    "hot chocolate": 100
}

valid_coin = [5, 10, 20, 50]


def select_drink():
    while True:
        choice = input("Choose a drink (coffee / tea / hot chocolate): ").lower()
        if choice in DRINKS:
            return DRINKS[choice]
        print("Invalid selection")


def get_coin():
    while True:
        try:
            coin = int(input("Insert a coin: ").replace("£", ""))
            if coin in valid_coin:
                return coin
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")


def update_total(current, coin):
    return current - coin


def calculate_change(amount):
    coins = [50, 20, 10, 5]
    change = []

    for coin in coins:
        while amount >= coin:
            change.append(coin)#single item to the end of a list.
            amount -= coin

    return change


def dispense_product(amount_due):
    if amount_due < 0:
        change = calculate_change(-amount_due)
        print("Returning:", ", ".join(f"{coin}p" for coin in change))
    else:
        print("Exact payment received. Thank you!")


def main():
    amount_due = select_drink()

    while amount_due > 0:
        coin = get_coin()
        amount_due = update_total(amount_due, coin)
        if amount_due > 0:
            print(f"Amount owed: £{amount_due}")

    dispense_product(amount_due)


main()
