SELECT
    ProductCategory.Name AS "Category Name",
    ProductSubcategory.Name AS "Subcategory Name",
    MIN(Product.ListPrice) AS "Lowest Price",
    MAX(Product.ListPrice) AS "Highest Price",
    MAX(Product.ListPrice) - MIN(Product.ListPrice) AS "Price Difference",
    COUNT(Product.ProductID) AS "Number of Products"
FROM
    Production.Product AS Product
JOIN
    Production.ProductSubcategory AS ProductSubcategory ON Product.ProductSubcategoryID = ProductSubcategory.ProductSubcategoryID
JOIN
    Production.ProductCategory AS ProductCategory ON ProductSubcategory.ProductCategoryID = ProductCategory.ProductCategoryID
GROUP BY
    ProductCategory.Name, ProductSubcategory.Name
ORDER BY
    ProductCategory.Name, ProductSubcategory.Name;