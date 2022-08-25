water = 300
milk = 200
coffee = 100
money = 0


def details():
    global water, milk, coffee, money
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")
    main()


def espresso():
    global water, milk, coffee, money
    e_water = 50
    e_coffee = 18
    e_price = 1.50

    if water < e_water and coffee < e_coffee:
        if water < e_water:
            print("Sorry there is not enough water.")
            print("Final details:")
            details()
            exit
        elif coffee < e_coffee:
            print("Sorry there is not enough coffee.")
            print("Final details:")
            details()
            exit
        else:
            pass

    elif water >= e_water and coffee >= e_coffee:
        print("Please enter coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        total_amount = ((0.1 * pennies) + (0.05 * nickles) + (0.10 * dimes) + (0.25 * quarters))

        if total_amount < e_price:
            print("Sorry that's not enough money. Money refunded.")
            main()
        elif total_amount > e_price:
            refund = total_amount - e_price

            money += e_price
            water -= e_water
            coffee -= e_coffee
            print(f"Here is {refund} in change.")
            print(f"Here is your espresso ☕ Enjoy!")
            main()
        elif total_amount == e_price:
            money += e_price
            water -= e_water
            coffee -= e_coffee
            print(f"Here is your espresso ☕ Enjoy!")
            main()
        else:
            pass

    else:
        pass


def latte():
    global water, milk, coffee, money
    l_water = 200
    l_coffee = 24
    l_milk = 150
    l_price = 2.50

    if water < l_water and coffee < l_coffee and milk < l_milk:
        if water < l_water:
            print("Sorry there is not enough water.")
            print("Final details:")
            details()
            exit
        elif coffee < l_coffee:
            print("Sorry there is not enough coffee.")
            print("Final details:")
            details()
            exit
        elif milk < l_milk:
            print("Sorry there is not enough milk.")
            print("Final details:")
            details()
            exit
        else:
            pass

    elif water >= l_water and coffee >= l_coffee and milk >= l_milk:
        print("Please enter coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        total_amount = ((0.1 * pennies) + (0.05 * nickles) + (0.10 * dimes) + (0.25 * quarters))

        if total_amount < l_price:
            print("Sorry that's not enough money. Money refunded.")
            main()
        elif total_amount > l_price:
            refund = total_amount - l_price

            money += l_price
            water -= l_water
            coffee -= l_coffee
            milk -= l_milk
            print(f"Here is {refund} in change.")
            print(f"Here is your latte ☕ Enjoy!")
            main()
        elif total_amount == l_price:
            money += l_price
            water -= l_water
            coffee -= l_coffee
            milk -= l_milk
            print(f"Here is your latte ☕ Enjoy!")
            main()
        else:
            pass

    else:
        pass


def cappuccino():
    global water, milk, coffee, money
    c_water = 250
    c_coffee = 24
    c_milk = 100
    c_price = 3

    if water < c_water and coffee < c_coffee and milk < c_milk:
        if water < c_water:
            print("Sorry there is not enough water.")
            print("Final details:")
            details()
            exit
        elif coffee < c_coffee:
            print("Sorry there is not enough coffee.")
            print("Final details:")
            details()
            exit
        elif milk < c_milk:
            print("Sorry there is not enough milk.")
            print("Final details:")
            details()
            exit
        else:
            pass

    elif water >= c_water and coffee >= c_coffee and milk >= c_milk:
        print("Please enter coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        total_amount = ((0.1 * pennies) + (0.05 * nickles) + (0.10 * dimes) + (0.25 * quarters))

        if total_amount < c_price:
            print("Sorry that's not enough money. Money refunded.")
            main()
        elif total_amount > c_price:
            refund = total_amount - c_price

            money += c_price
            water -= c_water
            coffee -= c_coffee
            milk -= c_milk
            print(f"Here is {refund} in change.")
            print(f"Here is your cappuccino ☕ Enjoy!")
            main()
        elif total_amount == c_price:
            money += c_price
            water -= c_water
            coffee -= c_coffee
            milk -= c_milk
            print(f"Here is your cappuccino ☕ Enjoy!")
            main()
        else:
            pass

    else:
        pass


def main():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "espresso":
        espresso()
    elif user_choice == "latte":
        latte()
    elif user_choice == "cappuccino":
        cappuccino()
    elif user_choice == "details":
        details()
    else:
        print("Invalid Input")
        main()


if __name__ == "__main__":
    print("""
   _____       __  __            __  __            _     _            
  / ____|     / _|/ _|          |  \/  |          | |   (_)           
 | |     ___ | |_| |_ ___  ___  | \  / | __ _  ___| |__  _ _ __   ___ 
 | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ /
 | |___| (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
  \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|                                                                
""")
    main()