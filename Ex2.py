class Category:
    def __init__(self, name, code, parent):
        self.name = name
        self.code = code
        self.no_of_product = 0
        self.parent = parent
        self.display_name = ""
        self.product = []

    def DisplayName(self):
        if self.parent is None:
            self.display_name = self.name
            return self.display_name
        else:
            self.display_name = self.parent.DisplayName() + ' > ' + self.name
            return self.display_name
        
    def AddProduct(self, products):
        self.product.append(products)    

    def PrintProduct(self):
        for i in range(len(self.product)):
            print(f"Name: {self.product[i].name} Code: {self.product[i].code} Category: {self.product[i].category.name}")
    
    def GroupBy():
        for i in cat_list:
            print(f"Category Name: {i.name}")
            for j in i.product:
                print(f"Name: {j.name} Code: {j.code}")

    def OrderBy():
        for i in range(len(cat_list)):
            for j in range(len(cat_list)):
                if cat_list[i].name<cat_list[j].name:
                    cat_list[i], cat_list[j] = cat_list[j], cat_list[i]            
        for i in cat_list:
            print(f"Category Name: {i.name}")
            for j in i.product:
                print(f"Name: {j.name} Code: {j.code}")
                
class Product:
    def __init__(self, name, code, category):
        self.name = name
        self.code = code
        self.category = category

c1 = Category("Vehicle", "C01", None)
c2 = Category("Car", "C02", c1)
c3 = Category("Petrol", "C03", c2)
c4 = Category("Diesel", "C04", c2)
c5 = Category("CNG", "C05", c2)

cat_list = [c1,c2,c3,c4,c5]

p1 = Product("Boat", "P01", c1)
p2 = Product("Bus", "P02", c1)
p3 = Product("Truck", "P03", c1)

p4 = Product("BMW", "P04", c2)
p5 = Product("Crete", "P05", c2)
p6 = Product("Verna", "P06", c2)

p7 = Product("Car", "P07", c3)
p8 = Product("Bike", "P08", c3)
p9 = Product("Truck", "P09", c3)

p10 = Product("D1", "P10", c4)
p11 = Product("D2", "P11", c4)
p12 = Product("D3", "P12", c4)

p13 = Product("C1", "P13", c5)
p14 = Product("C2", "P14", c5)
p15 = Product("C3", "P15", c5)

print(c1.DisplayName())
print(c2.DisplayName())
print(c3.DisplayName())
print(c4.DisplayName())
print(c5.DisplayName())

c1.AddProduct(p1)
c1.AddProduct(p2)
c1.AddProduct(p3)

c2.AddProduct(p4)
c2.AddProduct(p5)
c2.AddProduct(p6)

c3.AddProduct(p7)
c3.AddProduct(p8)
c3.AddProduct(p9)

c4.AddProduct(p10)
c4.AddProduct(p11)
c4.AddProduct(p12)

c5.AddProduct(p13)
c5.AddProduct(p14)
c5.AddProduct(p15)

c1.PrintProduct()
c2.PrintProduct()
c3.PrintProduct()
c4.PrintProduct()
c5.PrintProduct()
print("\n")
Category.GroupBy()
print("\n")
Category.OrderBy()