WITH RECURSIVE cnt (
    id
)
AS (
    SELECT EmployeeId
      FROM Employee
     WHERE FirstName = 'Andrew' AND 
           LastName = 'Adams'
    UNION
    SELECT EmployeeId
      FROM Employee,
           cnt
     WHERE Employee.ReportsTo = cnt.id
)
SELECT EmployeeId,
       FirstName,
       LastName,
       Title
  FROM Employee AS e,
       cnt
 WHERE e.EmployeeId = cnt.id
 ORDER BY e.EmployeeId;