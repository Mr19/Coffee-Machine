from Menu import MENU
from os import system, name
from time import sleep

resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

def clear():
    # cls for windows, posix for mac or linux
    system('cls') if name == 'nt' else system('clear')


def process_coins():
    print("Please insert coins.")
    quarters = int(input(f"how many quarters?: "))
    dimes = int(input(f"how many dimes?: "))
    nickles = int(input(f"how many nickles?: "))
    pennies = int(input(f"how many pennies?: "))
    coins_value = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
    return coins_value


def check_resources(coffee_type):
    for item in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(coffee_type):
    for item in MENU[coffee_type]["ingredients"]:
        resources[item] -= MENU[coffee_type]["ingredients"][item]
    print(f"Here is your {coffee_type} ☕️.Enjoy!")


def main():
    money_register = 0
    machine_maintenance = False
    while not machine_maintenance:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${money_register}')
            sleep(5)
            clear()
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            coffee_type = user_input
            cost = MENU[user_input]["cost"]
            if check_resources(coffee_type):
                coins_value = process_coins()
                if coins_value >= cost:
                    money_register += cost
                    print(f"Here is ${coins_value - cost} in change.")
                    make_coffee(coffee_type)
                    sleep(5)
                    clear()
                else:
                    print("Sorry that's not enough money. Money refunded.")
        elif user_input == "off":
            machine_maintenance = True
        else:
            clear()
            print("Please enter a valid response.")


if __name__ == '__main__':
    main()

