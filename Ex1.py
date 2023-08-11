class Category:
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.no_of_product = 0
       
    def print_info(self):
        print(f"Name: {self.name} Code: {self.code} No of product: {self.no_of_product}")

class Product:
    def __init__(self,name,code, category, price): 
        self.name = name
        self.code = code
        self.category = category
        self.price = price 
        category.no_of_product += 1
 
    def sort_high_to_low(products): # function for high to low price
        n = len(products)
        for i in range(n):
            for j in range(0, n - i - 1):
                if products[j].price < products[j + 1].price:
                    products[j], products[j + 1] = products[j + 1], products[j]

    def sort_low_to_high(products): # function for low to high price
        n = len(products)
        for i in range(n):
            for j in range(0, n - i - 1):
                if products[j].price > products[j + 1].price:
                    products[j], products[j + 1] = products[j + 1], products[j]   

    def search_code():
        search_code = input("Enter Code:") # searching product with its code
        found_product = None
        for product in product_list:
            if product.code == search_code:
                found_product = product
                break

        if found_product:
            print(f"\nProduct with code {search_code} found:")
            print(f"Name: {found_product.name}, Code: {found_product.code}, Category: {found_product.category.name}, Price: {found_product.price}")
        else:
            print(f"\nProduct with code {search_code} not found.")   

# creating three obj of category
c1 = Category("Stationary", "C01")
c2 = Category("Clothing", "C02")
c3 = Category("Food", "C03")

product_list = [] # creating 10 obj of product
product_list.append(Product("Book", "P01", c1, 100))
product_list.append(Product("Pen", "P02", c1, 90))
product_list.append(Product("Pencil", "P03", c1, 80))
product_list.append(Product("Tshrit", "P04", c2, 70))
product_list.append(Product("Shirt", "P05", c2, 60))
product_list.append(Product("Jacket", "P06", c2, 50))
product_list.append(Product("Jeans", "P07", c2, 40))
product_list.append(Product("Biscuit", "P08", c3, 30))
product_list.append(Product("Waffers", "P09", c3, 20))
product_list.append(Product("Chocolate", "P10", c3, 10))

print("=>Product category:")

cat = [c1,c2,c3]    
for i in cat:
    print(f"Name: {i.name} Code: {i.code} No of Products: {i.no_of_product}") # Printing category info

print("\n")
print("=>Product sorted in low to high:")

Product.sort_high_to_low(product_list) # sorting products in high to low price
for i in product_list:
    print(f"Name: {i.name} Code: {i.code} Price: {i.price}")

print("\n")
print("=>Product sorted in low to high:")

Product.sort_low_to_high(product_list) # sorting products in low to high price
for i in product_list:
    print(f"Name: {i.name} Code: {i.code} Price: {i.price}")

Product.search_code()