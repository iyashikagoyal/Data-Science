select Dim_Date.year, Dim_Date.month , SUM(Fact_Sale.unit_price * Fact_Sale.quantity)
    FROM Fact_Sale 
    JOIN Dim_Date on Fact_Sale.dim_date_id = Dim_Date.dim_date_id
    GROUP BY Dim_Date.year, Dim_Date.month;