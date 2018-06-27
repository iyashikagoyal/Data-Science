SELECT c.FirstName,
       c.LastName,
       SUM(il.UnitPrice) AS TotalMoneySpent,
       COUNT(il.Quantity) AS NoOfTracks
  FROM Invoice AS i
       JOIN
       Customer AS c ON c.CustomerId = i.CustomerId
       JOIN
       InvoiceLine AS il ON i.InvoiceId = il.InvoiceId
 GROUP BY c.CustomerId
 ORDER BY sum(il.UnitPrice) DESC
 LIMIT 1;