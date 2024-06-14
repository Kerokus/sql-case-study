SELECT
    EXTRACT(YEAR FROM SalesOrderHeader.OrderDate) AS "Year",
    EXTRACT(MONTH FROM SalesOrderHeader.OrderDate) AS "Month",
    COUNT(SalesOrderHeader.SalesOrderID) AS "Number of Shipped Orders",
    SUM(SalesOrderHeader.SubTotal) AS "Monthly Subtotal"
FROM
    Sales.SalesOrderHeader AS SalesOrderHeader
WHERE
    SalesOrderHeader.Status = 5 -- Status 5 corresponds to "Shipped"
GROUP BY
    EXTRACT(YEAR FROM SalesOrderHeader.OrderDate),
    EXTRACT(MONTH FROM SalesOrderHeader.OrderDate)
ORDER BY
    "Year", "Month";