SELECT
    Store.Name AS "Store Name",
    Customer.CustomerID AS "Customer ID",
    Store.BusinessEntityID AS "Store ID",
    SUM(SalesOrderHeader.SubTotal) AS "Total Amount Spent"
FROM
    Sales.SalesOrderHeader AS SalesOrderHeader
JOIN
    Sales.Customer AS Customer ON SalesOrderHeader.CustomerID = Customer.CustomerID
JOIN
    Sales.Store AS Store ON Customer.StoreID = Store.BusinessEntityID
WHERE
    SalesOrderHeader.Status = 5 -- Status 5 corresponds to "Shipped"
GROUP BY
    Store.Name,
    Customer.CustomerID,
    Store.BusinessEntityID
ORDER BY
    "Total Amount Spent" DESC;
