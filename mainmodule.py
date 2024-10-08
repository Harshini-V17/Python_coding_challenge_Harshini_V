from dao.orderprocessor import OrderProcessor
from entity.user import User
from entity.product import Product
from entity.electronics import Electronics
from entity.clothing import Clothing

class OrderManagement:
    def __init__(self):
        self.processor = OrderProcessor()
    
    def main(self):
        while True:
            print("\nOrder Management System")
            print("\nMenu:")
            print("1. Create User")
            print("2. Create Product")
            print("3. Create Order")
            print("4. Cancel Order")
            print("5. Get All Products")
            print("6. Get Orders by User")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.create_product()
            elif choice == '3':
                self.create_order()
            elif choice == '4':
                self.cancel_order()
            elif choice == '5':
                self.get_all_products()
            elif choice == '6':
                self.get_orders_by_user()
            elif choice == '7':
                print("Exiting the Order Management System!!!")
                break
            else:
                print("Invalid choice. Please enter a valid option!")
    
    def create_user(self):
        user_id = int(input("Enter user ID: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter the role (Admin/User): ")

        user = User(user_id, username, password, role)
        result = self.processor.createUser(user)
        if result:
            print(f"User {username} created successfully!")
        else:
            print("Failed to create user.")

    def create_product(self):
        user_id = int(input("Enter user ID: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (Admin/User): ")

        user = User(user_id, username, password, role)

        product_id = int(input("Enter product ID(ID number>0): "))
        product_name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantity_in_stock = int(input("Enter quantity in stock: "))
        type = input("Enter product type (Electronics/Clothing): ")
        if type == "Electronics":
                brand = input("Enter Electronics Brand: ")
                warranty_period = int(input("Enter Warranty Period (years): "))
                product = Electronics(product_id, product_name, description, price, quantity_in_stock,type, brand, warranty_period)
        elif type == "Clothing":
                size = input("Enter Clothing Size: ")
                color = input("Enter Clothing Color: ")
                product = Clothing(product_id, product_name, description, price, quantity_in_stock,type, size, color)
        else:
                print("Invalid product type.")
                
        result = self.processor.createProduct(user, product)
        if result:
            print(f"Product {product_name} created successfully!")
        else:
            print("Failed to create product.")

    def create_order(self):
        user_id = int(input("Enter user ID: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (Admin/User): ")

        user = User(user_id, username, password, role)
        products = []
        while True:
            product_id = int(input("Enter product ID (Enter 0 to finish): "))
            if product_id == 0:
                break

            product_quantity = int(input("Enter product quantity: "))
            product = Product(product_id, "", "", 0, 0, "")
            product.quantity = product_quantity
            products.append(product)

        result = self.processor.createOrder(user, products)
        if result:
            print("Order created successfully.")
        else:
            print("Failed to create order.")

    def cancel_order(self):
        user_id = int(input("Enter user ID: "))
        order_id = int(input("Enter order ID: "))

        result = self.processor.cancelOrder(user_id, order_id)
        if result:
            print(f"Order {order_id} cancelled successfully!")
        else:
            print("Failed to cancel order.")

    def get_all_products(self):
        products = self.processor.getAllProducts()
        if products:
            print("Products list:")
            for product in products:
                print(product)
        else:
            print("Failed to retrieve products.")

    def get_orders_by_user(self):
        user_id = int(input("Enter user ID: "))
        user = User(user_id, "", "", "")

        orders = self.processor.getOrderByUser(user)
        if orders:
            print(f"Orders for user with ID {user_id}:")
            for order in orders:
                print(order)
        else:
            print("No orders found for the user.")

def main():
    order_management = OrderManagement()
    order_management.main()

if __name__ == "__main__":
    main()