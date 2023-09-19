#python oop
#defensive programming

class Product: # product class
    def __init__(self, name, price):
        self.name = name # name attribute
        self.price = price # price attribute

class ShoppingCart: # shopping cart class
    def __init__(self, user_balance=0):
        self.user_balance = user_balance # user balance attribute
        self.products = [] # products attribute

    def add_product(self, product):  # method to add product
        if product.price <= self.user_balance:
            self.products.append(product)
            self.user_balance -= product.price
            print(f"Added {product.name} to the cart: Price: ₱{product.price}")
        else:
            print("Insufficient balance to add the product.")

    def list_products(self): # method for listing products currently in cart
        if self.products:
            print("\nProducts in the cart:")
            for index, product in enumerate(self.products):
                print(f"{index + 1}. {product.name} - ₱{product.price}")
        else:
            print("Your cart is empty.")

    def purchase_product(self, index): # method that allows user to purchase product from the cart if they have enough balance
        if 0 <= index < len(self.products):
            product = self.products[index]
            if product.price <= self.user_balance:
                self.user_balance -= product.price
                del self.products[index]
                print(f"\nPurchased {product.name}. Available balance: ₱{self.user_balance}")
            else:
                print("Insufficient balance to purchase the product.")
        else:
            print("Invalid product index.")

#create a ShoppingCart object with an initial user balance
my_cart = ShoppingCart(user_balance=1005352) # balance instance

#create Product instances
laptop = Product("Laptop", 89000)
phone = Product("Phone", 10000)
keyboard = Product("Keyboard", 10000)
mouse = Product("Mouse", 1000)

# add products to the cart
my_cart.add_product(laptop)
my_cart.add_product(phone)
my_cart.add_product(keyboard)
my_cart.add_product(mouse)

#list products in the cart
my_cart.list_products()

#Purchase product from the cart
my_cart.purchase_product(0)

#List updated products in the cart
my_cart.list_products()

#end