SELECT
    CASE 
        WHEN Product.ListPrice BETWEEN 0 AND 50 THEN '0 - 50'
        WHEN Product.ListPrice BETWEEN 50 AND 100 THEN '50 - 100'
        WHEN Product.ListPrice BETWEEN 100 AND 200 THEN '100 - 200'
        WHEN Product.ListPrice BETWEEN 200 AND 500 THEN '200 - 500'
        WHEN Product.ListPrice BETWEEN 500 AND 1000 THEN '500 - 1000'
        ELSE '1000+'
    END AS "Price Bracket",
    COUNT(Product.ProductID) AS "Number of Products"
FROM
    Production.Product AS Product
GROUP BY
    CASE 
        WHEN Product.ListPrice BETWEEN 0 AND 50 THEN '0 - 50'
        WHEN Product.ListPrice BETWEEN 50 AND 100 THEN '50 - 100'
        WHEN Product.ListPrice BETWEEN 100 AND 200 THEN '100 - 200'
        WHEN Product.ListPrice BETWEEN 200 AND 500 THEN '200 - 500'
        WHEN Product.ListPrice BETWEEN 500 AND 1000 THEN '500 - 1000'
        ELSE '1000+'
    END
ORDER BY
    "Number of Products";
