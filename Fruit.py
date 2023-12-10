class Fruit:
    """Object definition for the class Fruit"""
    
    def __init__(self, name, form, retail_price, stock_quantity):
        """Method to initialize the attributes"""
        self.name = name
        self.form = form
        self.retail_price = retail_price
        self.stock_quantity = stock_quantity

    def __str__(self):
        """Method to return a fruit object as a string"""
        return self.name + "-" + self.form + " : $" + f"{self.retail_price:.2f}" + " per pound; stock: " + \
            str(self.stock_quantity) + " pounds"

    def change_retail_price(self, new_price):
        """Method to change the retail price of a fruit object"""
        original_retail_price = self.retail_price
        self.retail_price = new_price

        # return removed/changed data
        return original_retail_price

    def __eq__(self, fruit):
        """Method to change that determines the equality between two fruit objects"""
        return self.name == fruit.name and self.form == fruit.form and \
            self.retail_price == fruit.retail_price and self.stock_quantity == fruit.stock_quantity

    def eq_ignore_price_and_stock(self, fruit):
        """Method to change that determines the equality between two fruit objects, ignoring price and stock value"""
        return self.name == fruit.name and self.form == fruit.form

    def eq_ignore_stock(self, fruit):
        """Method to change that determines the equality between two fruit objects, ignoring stock value"""
        return self.name == fruit.name and self.form == fruit.form and \
            self.retail_price == fruit.retail_price
