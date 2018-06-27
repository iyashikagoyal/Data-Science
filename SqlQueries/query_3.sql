SELECT e.EmployeeId,
       e.FirstName,
       e.LastName,
       e.Title,
       COUNT(c.SupportRepid) as NumberOfCustomerSupported 
  FROM Employee AS e
       JOIN
       Customer AS c ON e.EmployeeId = c.SupportRepid
 GROUP BY c.SupportRepid
HAVING COUNT(c.SupportRepid) = (
                                   SELECT MAX(cust_count) 
                                     FROM (
                                              SELECT COUNT(SupportRepid) AS cust_count
                                                FROM CUSTOMER
                                               GROUP BY SupportRepid
                                          )
                               );