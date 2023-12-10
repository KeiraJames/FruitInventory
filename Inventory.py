from Fruit import Fruit

class Inventory(Fruit):
    """ Object definition for the class Fruit """

    def __init__(self):
        self.fruit_inventory_list = []

    def is_empty(self):
        # boolean method to check if inventory list is empty
        return len(self.fruit_inventory_list) == 0

    def add_fruit(self, fruit_name, form, retail_price, quantity):
        
        fruit = Fruit(name=fruit_name, form=form, retail_price=retail_price, stock_quantity=quantity)

        if self.is_empty():
            # letting user know the fruit was not in stock and has been added
            print("Item not in stock, inventory has been adjusted to add " + fruit.name + "-" + fruit.form)
            self.fruit_inventory_list.append(fruit)
            return

        for item in range(len(self.fruit_inventory_list)):
           
            if self.fruit_inventory_list[item].eq_ignore_stock(fruit):
        
                print("The item " + fruit.name + "-" + fruit.form + " is already in stock, stock has been adjusted.")
                self.fruit_inventory_list[item].stock_quantity += fruit.stock_quantity
                return

        # if you fall out of the loop and fruit isn't there, add it
        print("Item not in stock, inventory has been adjusted to add " + fruit.name + "-" + fruit.form + ".")
        self.fruit_inventory_list.append(fruit)


    def remove_fruit(self, fruit_name, form, quantity):
       
        fruit = Fruit(name=fruit_name, form=form, retail_price=None, stock_quantity=quantity)

        for item in range(len(self.fruit_inventory_list)):
           
            if self.fruit_inventory_list[item].eq_ignore_price_and_stock(fruit):

                # decrease stock by desired amount
                self.fruit_inventory_list[item].stock_quantity = \
                    self.fruit_inventory_list[item].stock_quantity - fruit.stock_quantity

                # check if the quantity is negative or equal to 0, if so then remove it
                if self.fruit_inventory_list[item].stock_quantity <= 0:
                    self.fruit_inventory_list.remove(self.fruit_inventory_list[item])
                    break


    def display_inventory(self):
        if self.is_empty():
            print("No fruits in the inventory.")
            return

        for item in range(len(self.fruit_inventory_list)):
            print("Item ", item + 1, "=\t", self.fruit_inventory_list[item])

    def make_purchase(self, cart):

        running_total = 0

        for i in range(len(cart)):

            found_fruit = False

            for j in range(len(self.fruit_inventory_list)):

                if self.fruit_inventory_list[j].eq_ignore_price_and_stock(cart[i]):

                    # if we found a match in the inventory, change to True
                    found_fruit = True

                    # check to see if we have enough items in stock to be purchased first
                    # if num is negative, that means we didn't have the requested amount available
                    num = self.fruit_inventory_list[j].stock_quantity - cart[i].stock_quantity

                    # remove items from stock
                    self.remove_fruit(fruit_name=cart[i].name, form=cart[i].form, quantity=cart[i].stock_quantity)

                    if not num < 0:

                        # if we didn't run out of the item, compute total normally
                        running_total += (cart[i].retail_price * cart[i].stock_quantity)
                    else:

                        # if we did run out, see how much stock we actually had available
                        cart[i].stock_quantity -= abs(num)

                        # let user know how much they could've purchased
                        print("Only able to purchase " + str(cart[i].stock_quantity) + " of the " +
                              str((cart[i].stock_quantity + abs(num))) + " " + str(cart[i].name) + "s requested.")

                        running_total += cart[i].retail_price * cart[i].stock_quantity

                    break

            if not found_fruit:

                # let user know if an item in their cart isn't in the inventory at all
                print("The item " + str(cart[i].name) + "-" + str(cart[i].form) + " is not in stock.")

        return "Total purchase amount: $" + f"{running_total:.2f}"
