from dao.Repository import OrderManagementRepository
from entity.user import User
from entity.product import Product
from util.db_util import DBUtil
from exception.UserNotFound import UserNotFound
from exception.OrderNotFound import OrderNotFound

class OrderProcessor(OrderManagementRepository):
    def __init__(self):
        self.db_util = DBUtil()

    def createOrder(self, user: User, products: list):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            # Insert user if not exists
            cursor.execute("IF NOT EXISTS (SELECT * FROM order_User WHERE UserId = ?) INSERT INTO order_User (UserId, Username, Password, Role) VALUES (?, ?, ?, ?)", 
                           user.userId, user.userId, user.username, user.password, user.role)
            
            # Insert order
            cursor.execute("INSERT INTO system_order ( UserId) OUTPUT INSERTED.OrderId VALUES (?)", user.getUserId())
                
            order_id = cursor.fetchone()[0]

            # Insert products for the order
            for product in products:
                cursor.execute("INSERT INTO OrderProduct (OrderId, ProductId, Quantity) VALUES (?, ?, ?)", order_id, product.productId, product.quantity)

            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def cancelOrder(self, userId: int, orderId: int):
        try:
            connection = DBUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM order_User WHERE userId = ?", userId)
                user_count = cursor.fetchone()[0]
                if user_count == 0:
                    raise UserNotFound(f"User with ID {userId} not found.")

                cursor.execute("SELECT COUNT(*) FROM system_order WHERE userId = ? AND orderId = ?", userId, orderId)
                order_count = cursor.fetchone()[0]
                if order_count == 0:
                    raise OrderNotFound(f"Order with ID {orderId} not found for user {userId}.")
                cursor.execute("DELETE FROM OrderProduct WHERE orderId = ?", orderId)
                cursor.execute("DELETE FROM system_order WHERE userId = ? AND orderId = ?", userId, orderId)
                connection.commit()
                print("Order cancelled successfully.")
            else:
                print("Failed to connect to database.")
        except UserNotFound as e:
            print("Error :", e)
        except OrderNotFound as e:
            print("Error :", e)
        except Exception as e:
            print("Error :", e)
        finally:
            if connection:
                connection.close()

    def createProduct(self, user: User, product: Product):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            # Check if the user is admin
            if user.role != "Admin":
                print("Only admin users can create products.")
                return False
            
            cursor.execute("INSERT INTO order_Product (ProductId, ProductName, Description, Price, QuantityInStock, Type) VALUES (?, ?, ?, ?, ?, ?)", 
                           product.productId, product.productName, product.description, product.price, product.quantityInStock, product.type)
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def createUser(self, user: User):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO order_User (UserId, Username, Password, Role) VALUES (?, ?, ?, ?)", user.userId, user.username, user.password, user.role)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def getAllProducts(self):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM order_Product")
            products = cursor.fetchall()
            conn.close()
            return products
        except Exception as e:
            print("Error:", e)
            return None

    def getOrderByUser(self, user: User):
        try:
            conn = self.db_util.getDBConn()
            cursor = conn.cursor()

            # Query to retrieve order details including product name and quantity bought
            query = """
            SELECT o.OrderId, p.ProductName, op.Quantity
            FROM system_order o
            JOIN OrderProduct op ON o.OrderId = op.OrderId
            JOIN order_Product p ON op.ProductId = p.ProductId
            WHERE o.UserId = ?
            """

            cursor.execute(query, user.userId)
            orders = cursor.fetchall()
            conn.close()
            return orders
        except Exception as e:
            print("Error:", e)
            return None