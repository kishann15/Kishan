class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        

class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location   = to_location
        self.product       = product
        self.quantity      = quantity

    @staticmethod
    def movement_by_product(product):
        for item in movements:
            if item.product==product:
                if item.quantity > product.stock_at_location[item.from_location]:
                    raise Exception("No stock available!")
                product.stock_at_location[item.from_location] -= item.quantity
                product.stock_at_location[item.to_location] += item.quantity
                print(f"{product.name} moved from {item.from_location} to {item.to_location} with quantity {item.quantity}")


class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.stock_at_location = {}

    def PrintProduct():
        for product in products:
            print(product.name, product.stock_at_location)

    def GroupBy():
        for i in locations:
            print(i.name)
            for j in products:
                if j.stock_at_location[i.name]:
                    print(f" {j.name} {j.stock_at_location[i.name]}")

locations = []
locations.append(Location("Junagadh","A01"))
locations.append(Location("Rajkot","B01"))
locations.append(Location("Ahmedabad","C01"))
locations.append(Location("Surat","D01"))                                

p1 = Product("Smart Phones", "P01")
p1.stock_at_location = {
    "Junagadh":10,
    "Rajkot":20,
    "Ahmedabad":30,
    "Surat":40
}

p2 = Product("Food", "P02")
p2.stock_at_location = {
    "Junagadh":20,
    "Rajkot":30,
    "Ahmedabad":40,
    "Surat":10
}

p3 = Product("Cloths", "P03")
p3.stock_at_location = {
    "Junagadh":30,
    "Rajkot":40,
    "Ahmedabad":10,
    "Surat":20
}

p4 = Product("Laptops", "P04")
p4.stock_at_location = {
    "Junagadh":40,
    "Rajkot":10,
    "Ahmedabad":20,
    "Surat":30
}

p5 = Product("Headphones", "P05")
p5.stock_at_location = {
    "Junagadh":10,
    "Rajkot":20,
    "Ahmedabad":30,
    "Surat":40
}

products = [p1,p2,p3,p4,p5]

m1 = Movement("Junagadh", "Rajkot", p1, 5)
m2 = Movement("Rajkot", "Ahmedabad", p2 , 5)
m3 = Movement("Ahmedabad", "Surat", p3, 5)
m4 = Movement("Surat", "Junagadh", p4, 5)
m5= Movement("Junagadh", "Rajkot", p5, 5)

movements = [m1,m2,m3,m4,m5]

Product.PrintProduct()

print("\n")
Movement.movement_by_product(p1)
print("\n")
Movement.movement_by_product(p2)
print("\n")
Movement.movement_by_product(p3)
print("\n")
Movement.movement_by_product(p4)
print("\n")
Movement.movement_by_product(p5)
print("\n")

Product.GroupBy()