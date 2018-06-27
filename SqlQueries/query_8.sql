SELECT strftime('%Y-%m', i.InvoiceDate) AS Month,
       SUM(il.UnitPrice * il.Quantity) AS TotalRevenue
  FROM Invoice AS i
       JOIN
       InvoiceLine AS il ON i.InvoiceId = il.InvoiceId
 GROUP BY strftime('%Y-%m', i.InvoiceDate) 
 ORDER BY SUM(il.UnitPrice * il.Quantity) DESC
 LIMIT 1;