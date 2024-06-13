-- Define the threshold for vacation hours
WITH Threshold AS (
    SELECT 40 AS MinVacationHours
)

-- Primary Datas
SELECT
    CONCAT(Person.LastName, ', ', Person.FirstName) AS "Employee Name",
    Employee.JobTitle AS "Position",
    EmailAddress.EmailAddress AS "Email Address",
    Employee.VacationHours AS "Vacation Hours Accrued"
FROM
    HumanResources.Employee AS Employee
JOIN
    Person.Person AS Person ON Employee.BusinessEntityID = Person.BusinessEntityID
JOIN
    HumanResources.EmployeeDepartmentHistory AS EmployeeDeptHistory ON Employee.BusinessEntityID = EmployeeDeptHistory.BusinessEntityID
JOIN
    -- Get the latest start date for each employee
    (
        SELECT 
            BusinessEntityID, 
            MAX(StartDate) AS MaxStartDate
        FROM 
            HumanResources.EmployeeDepartmentHistory
        GROUP BY 
            BusinessEntityID
    ) AS LatestDeptHistory ON 
        EmployeeDeptHistory.BusinessEntityID = LatestDeptHistory.BusinessEntityID AND 
        EmployeeDeptHistory.StartDate = LatestDeptHistory.MaxStartDate
JOIN
    Person.EmailAddress AS EmailAddress ON Employee.BusinessEntityID = EmailAddress.BusinessEntityID
JOIN
    Threshold AS Threshold ON Employee.VacationHours > Threshold.MinVacationHours
ORDER BY
    "Employee Name";