from entity.product import Product

class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.size = size
        self.color = color
    
    # Getters
    def getSize(self):
        return self.size
    
    def getColor(self):
        return self.color
    
    # Setters
    def setSize(self, size):
        self.size = size
    
    def setColor(self, color):
        self.color = color