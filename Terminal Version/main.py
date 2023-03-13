import csv
from datetime import datetime

with open('Menu.txt', 'w') as f:
    f.write('* Please Choose a Pizza Base:\n1: Classic\n2: Margherita\n3: TurkPizza\n4: PlainPizza\n')
    f.write('* and sauce of your choice:\n11: Olives\n12: Mushrooms\n13: GoatCheese\n14: Meat\n15: Onions\n16: Corn\n')
    f.write('* Thank you!\n')


# pizza superclassını olusturduk
class Pizza:
    def get_description(self):
        pass

    def get_cost(self):
        pass


# subclasslar
class ClassicPizza(Pizza):
    price = 15.99
    description = "Classic Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class MargheritaPizza(Pizza):
    price = 17.99
    description = "Margherita Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class TurkPizza(Pizza):
    price = 19.99
    description = "Turk Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class PlainPizza(Pizza):
    price = 12.99
    description = "Plain Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


# decorator superclasini olusturduk
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + " " + Pizza.get_description(self)


# decorator subclasslari
class Olives(Decorator):
    price = 1.50
    description = "with Olives"

    def __init__(self, component):
        Decorator.__init__(self, component)

    def get_cost(self):
        return self.component.get_cost() + self.price

    def get_description(self):
        return self.component.get_description() + " " + self.description


class Mushrooms(Decorator):
    price = 1.25
    description = "with Mushrooms"

    def __init__(self, component):
        Decorator.__init__(self, component)

    def get_cost(self):
        return self.component.get_cost() + self.price

    def get_description(self):
        return self.component.get_description() + " " + self.description


class GoatCheese(Decorator):
    price = 2.25
    description = "with Goat Cheese"

    def __init__(self, component):
        Decorator.__init__(self, component)

    def get_cost(self):
        return self.component.get_cost() + self.price

    def get_description(self):
        return self.component.get_description() + " " + self.description


class Meat(Decorator):
    price = 2.50
    description = "with Meat"

    def __init__(self, component):
        Decorator.__init__(self, component)

    def get_cost(self):
        return self.component.get_cost() + self.price

    def get_description(self):
        return self.component.get_description() + " " + self.description


class Onions(Decorator):
    price = 1.00
    description = "with Onions"

    def __init__(self, component):
        Decorator.__init__(self, component)

    def get_cost(self):
        return self.component.get_cost() + self.price

    def get_description(self):
        return self.component.get_description() + " " + self.description


class Corn(Decorator):
    price = 1.00
    description = "with Corn"

    def __init__(self, component):
        Decorator.__init__(self, component)

    def get_cost(self):
        return self.component.get_cost() + self.price

    def get_description(self):
        return self.component.get_description() + " " + self.description


# Ekrana menuyu yazdiracak fonksiyon tanımladık
def print_menu():
    with open('Menu.txt', 'r') as FILE:
        menu = FILE.read()
        print(menu)


if __name__ == '__main__':
    print_menu()
    # Kullanicilarin secim islemleri
    while True:
        try:
            pizza_choice = int(input("Please enter the number of the pizza you would like to order: "))
            if pizza_choice < 1 or pizza_choice > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please try again.")

    pizza = None
    if pizza_choice == 1:
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = PlainPizza()
    else:
        print("Invalid choice.")
        exit()

    print("Please select a sauce:")
    print("11: Olives")
    print("12: Mushrooms")
    print("13: Goat Cheese")
    print("14: Meat")
    print("15: Onions")
    print("16: Corn")

    sauce_choice = int(input("Enter sauce choice: "))
    if sauce_choice == 11:
        pizza = Olives(pizza)
        print("Olives selected.")
    elif sauce_choice == 12:
        pizza = Mushrooms(pizza)
        print("Mushrooms selected.")
    elif sauce_choice == 13:
        pizza = GoatCheese(pizza)
        print("Goat Cheese selected.")
    elif sauce_choice == 14:
        pizza = Meat(pizza)
        print("Meat selected.")
    elif sauce_choice == 15:
        pizza = Onions(pizza)
        print("Onions selected.")
    elif sauce_choice == 16:
        pizza = Corn(pizza)
        print("Corn selected.")
    else:
        print("Invalid choice.")
        exit()

    print("\nYour order is:")
    print(pizza.get_description())
    print("Total cost: $" + str(pizza.get_cost()))

    name = input("Please enter your name: ")
    id_number = input("Please enter your ID number: ")
    credit_card_number = input("Please enter your credit card number: ")
    credit_card_password = input("Please enter your credit card password: ")
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Orders_Database.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow([name, id_number, credit_card_number, credit_card_password,str(pizza.get_description()), str(pizza.get_cost()), order_time])
