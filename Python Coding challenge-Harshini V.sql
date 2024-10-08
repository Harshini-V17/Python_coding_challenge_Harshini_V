create database system;
use system;

CREATE TABLE order_User ( 
UserId INT PRIMARY KEY, 
Username NVARCHAR(100), 
Password NVARCHAR(100), 
Role NVARCHAR(50) );

CREATE TABLE order_Product ( 
ProductId INT PRIMARY KEY, 
ProductName NVARCHAR(100), 
Description NVARCHAR(MAX), 
Price DECIMAL(10, 2), 
QuantityInStock INT, 
Type NVARCHAR(50), );

CREATE TABLE system_order ( 
OrderId INT IDENTITY(1, 1) PRIMARY KEY, 
UserId INT FOREIGN KEY REFERENCES order_User (UserId) );


CREATE TABLE OrderProduct ( 
OrderId INT, 
ProductId INT, 
Quantity INT, 
PRIMARY KEY (OrderId, ProductId), 
FOREIGN KEY (OrderId) REFERENCES system_order (OrderId), 
FOREIGN KEY (ProductId) REFERENCES order_Product(ProductId) );