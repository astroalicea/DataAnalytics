northwind_review




# Northwind Database Review

## Categories
- PK: CategoryID
- No Foreign Keys
- Represents: Product categories (Beverages, Seafood, etc.)
- Useful columns: CategoryID, CategoryName

## Customers
- PK: CustomerID
- No Foreign Keys
- Represents: Companies that place orders
- Useful columns: CustomerID, CompanyName, City, Country, Region

## Employees
- PK: EmployeeID
- FK: ReportsTo → Employees (self-referencing)
- Represents: Company staff who handle orders
- Useful columns: EmployeeID, FirstName, LastName, Title, City, Country

## EmployeeTerritories
- PK: EmployeeID + TerritoryID (composite)
- FK: EmployeeID → Employees, TerritoryID → Territories
- Represents: Which territories each employee covers

## Orders
- PK: OrderID
- FK: CustomerID → Customers, EmployeeID → Employees, ShipVia → Shippers
- Represents: Each order placed by a customer
- Useful columns: OrderID, CustomerID, EmployeeID, OrderDate, ShippedDate, Freight

## Order Details
- PK: OrderID + ProductID (composite)
- FK: OrderID → Orders, ProductID → Products
- Represents: Individual line items within an order
- Useful columns: OrderID, ProductID, UnitPrice, Quantity, Discount

## Products
- PK: ProductID
- FK: CategoryID → Categories, SupplierID → Suppliers
- Represents: Items available for sale
- Useful columns: ProductID, ProductName, UnitPrice, UnitsInStock

## Region
- PK: RegionID
- No Foreign Keys
- Represents: Geographic sales regions

## Shippers
- PK: ShipperID
- No Foreign Keys
- Represents: Companies that ship orders
- Useful columns: ShipperID, CompanyName

## Suppliers
- PK: SupplierID
- No Foreign Keys
- Represents: Companies that supply products
- Useful columns: SupplierID, CompanyName, City, Country, Region

## Territories
- PK: TerritoryID
- FK: RegionID → Region
- Represents: Sales territories within regions
- Useful columns: TerritoryID, TerritoryDescription, RegionID