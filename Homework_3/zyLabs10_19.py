# Syed Shams
# 1820287

class ItemsToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        # function to print the item name, cost, and quantity
        print(self.item_name + " " + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $' +
              str(int(self.item_price * self.item_quantity)))

    def print_item_description(self):
        # Addition of another attribute for this class
        print("{}: {}".format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, string):
        print("\nADD ITEM TO CART")
        print('Enter the item name:')
        item_name = input()
        print('Enter the item description:')
        item_description = input()
        print('Enter the item price:')
        item_price = int(input())
        print('Enter the item quantity')
        item_quantity = int(input())

        self.cart_items.append(ItemsToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):
        print('\nREMOVE ITEM FROM CART')
        print('Enter name of item to remove:')
        remove_item_name = input()
        counter = False

        for item in self.cart_items:
            if item.item_name == remove_item_name:
                self.cart_items.remove(item)
                counter = True
                break
            if not counter:
                print('Item not found in the cart. Nothing removed')

    def modify_item(self):
        print('\nCHANGE ITEM QUANTITY')
        name = input('Enter the item name:')
        print('Enter the new quantity:')
        quantity = int(input())
        counter = False
        for item in self.cart_items:
            if name == item.item_name:
                item.item_quantity = quantity
                counter = True
                break
        if not counter:
            print('Item not found in the cart. Nothing modified')

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    def print_description(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
            print('\nItem Descriptions', end='\n')

            for item in self.cart_items:
                item.print_item_description()

    def output_cart(self):
        print('\nOUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', self.get_num_items_in_cart())
        if len(self.cart_items) == 0:
            print('\nSHOPPING CART IS EMPTY')
            print()
            print("Total: $0")
        else:
            counter = 0
            for item in self.cart_items:
                print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity, item.item_price,
                                                 (item.item_quantity * item.item_price)), end='\n')
                counter += (item.item_quantity * item.item_price)
            print('\nTotal: ${}'.format(counter))


def print_menu(cart):
    customer_cart = cart
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')
    command = ''
    while command != 'q':
        string = ''
        print(menu, end='\n')
        print('Choose an option:')
        command = input()
        while command != 'a' and command != 'o' and command != 'i' and command != 'q' and command != 'r' and command != 'c':
            print('Choose an option:')
            command = input()
        if command == 'a':
            customer_cart.add_item(string)
        if command == 'o':
            customer_cart.output_cart()
        if command == 'i':
            customer_cart.print_descriptions()
        if command == 'r':
            customer_cart.remove_item()
        if command == 'c':
            customer_cart.modify_item()


if __name__ == "__main__":
    print('Enter customer\'s name:')
    customer_name = input()
    print('Enter today\'s date:')
    current_date = input()
    print()
    print("Customer name:", customer_name)
    print('Today\'s date:', current_date)
    Cart = ShoppingCart(customer_name, current_date)
    print_menu(Cart)
