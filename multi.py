#multiple inheritance:
 
#class 1
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
       
    def show_details(self):
        print(f"Product: {self.name}, Price: INR. {self.price}")
       
# class -2    
class Supplier:
    def __init__(self,supplier_name):
        self.supplier_name = supplier_name
       
    def  show_supplier(self):
        print(f"Supplier: {self.supplier_name}")
       
 
class Electronics(Product,Supplier):
    def __init__(self,name,price,supplier_name,brand):
        Supplier.__init__(self,supplier_name)
        Product.__init__(self,name,price)
        self.brand = brand
       
    def show_display(self):
        self.show_details()
        self.show_supplier()
        print(f" the brand is {self.brand}")
       
       
e = Electronics("Laptop", 12000, "ABC Pvt Ltd.","Samsung")
e.show_display()
 