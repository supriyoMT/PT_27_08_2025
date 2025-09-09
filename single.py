class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
       
    def show_details(self):
        print(f"Product: {self.name}, Price: INR. {self.price}")
       
   
class Electronics(Product):
    def __init__(self,name,price,warranty):
        super().__init__(name,price)
        self.warranty = warranty
       
    def show_electronics(self):
        self.show_details()
        print(f"Warranty: {self.warranty}")
       
e = Electronics("Laptop", 12000, 3)
e.show_electronics()