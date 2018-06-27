CREATE TABLE Fact_Sale AS SELECT c.City,
                                 il.InvoiceLineId AS dim_sale_id,
                                 i.InvoiceId AS dim_date_id,
                                 c.CustomerId AS dim_location_id,
                                 t.Trackid AS dim_track_id,
                                 il.unitprice AS unit_price,
                                 il.quantity
                            FROM (
                                     customer c
                                     JOIN
                                     invoice i ON c.CustomerId = i.CustomerId
                                     JOIN
                                     invoiceline il ON il.InvoiceId = i.InvoiceId
                                     JOIN
                                     track t ON t.TrackId = il.TrackId
                                 );
