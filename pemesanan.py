import os

class MenuItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.stock} left in stock"

class Menu:
    def __init__(self):
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to our menu!")
        for menu_item in self.menu_items:
            print(menu_item)
        print("\n")

    def find_menu_item(self, name):
        for menu_item in self.menu_items:
            if menu_item.name.lower() == name.lower():
                return menu_item
        return None

    def handle_order(self, order):
        total_cost = 0
        for item in order:
            menu_item = self.find_menu_item(item)
            if menu_item is not None:
                if menu_item.stock > 0:
                    total_cost += menu_item.price
                    menu_item.stock -= 1
                else:
                    print(f"Sorry, {item} is out of stock!")
            else:
                print(f"Sorry, we do not have {item}.")
        print(f"\nYour total bill is: ${total_cost}")

menu = Menu()
menu.add_menu_item(MenuItem("Burger", 5, 10))
menu.add_menu_item(MenuItem("Fries", 2, 5))
menu.add_menu_item(MenuItem("Coke", 1, 20))

while True:
    menu.display_menu()
    print("Enter the items you want to order, separated by spaces. Type 'quit' to exit.")
    order = input().split()
    if order[0].lower() == 'quit':
        break
    menu.handle_order(order)
