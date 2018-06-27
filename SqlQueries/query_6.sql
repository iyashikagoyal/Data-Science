SELECT mgr.EmployeeId ,
       mgr.FirstName,
       mgr.LastName,
       mgr.Title,
       count(mgr.lastname) AS NoOfReports
  FROM employee e
       LEFT JOIN
       employee mgr ON e.reportsto = mgr.employeeid
 GROUP BY mgr.lastname
 ORDER BY count(mgr.lastname) DESC
 LIMIT 1;