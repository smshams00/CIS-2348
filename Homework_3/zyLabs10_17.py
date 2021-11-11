# Syed Shams
# 1820287

class ItemsToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        # function to print the item name, cost, and quantity
        print(self.item_name + " " + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $' +
              str(int(self.item_price * self.item_quantity)))


if __name__ == "__main__":
    item1 = ItemsToPurchase()  # Item 1 object created
    print("Item 1\nEnter the item name:")
    item1.item_name = input()
    print("Enter the item price:")
    item1.item_price = int(input())
    print("Enter the item quantity:")
    item1.item_quantity = int(input())

    item2 = ItemsToPurchase()  # Item 2 object created
    print("\nItem 2\nEnter the item name:")
    item2.item_name = input()
    print("Enter the item price:")
    item2.item_price = int(input())
    print("Enter the item quantity:")
    item2.item_quantity = int(input())

    print("\nTOTAL COST")

    item1.print_item_cost()  # Call the print_item_cost for object Item 1
    item2.print_item_cost()  # Call the print_item_cost for object Item 2

    total_cost = str((item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity))

    print("\nTotal: $" + total_cost)
