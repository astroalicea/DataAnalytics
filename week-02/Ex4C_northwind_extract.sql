USE northwind;

-- 4 a) The table that holds the items Northwind sells is the products table.
-- 4 b) The table that holds the categories of items is the categories table.

-- 5 a) Peacock Margaret

SELECT * FROM products;
-- To limit rows using the toolbar: change the "Limit to 1000 rows" 
-- dropdown at the top of the query pane to 10.

-- 6 a) 77 

SELECT * FROM categories;
-- 7 a) seafood is number 8
SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders