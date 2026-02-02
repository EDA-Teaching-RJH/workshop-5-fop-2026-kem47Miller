#statement of requirements
cost = 75
valid_coin = [5, 10, 20, 50]


def get_coin():
    """Handles input and validation."""
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
    """Performs simple calculation."""
    return current - coin


def dispense_product(amount_due):
    """Handles output."""
    if amount_due < 0:
        print(f"Your change: £{-amount_due}")
    else:
        print("Amount paid!")


def main():
    amount_due = cost
    while amount_due > 0:
        coin = get_coin()
        amount_due = update_total(amount_due, coin)
        if amount_due > 0:
            print(f"Amount owed: £{amount_due}")
    dispense_product(amount_due)


main()
