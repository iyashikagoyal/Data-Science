CREATE TABLE Dim_Date AS SELECT InvoiceId AS dim_date_id,
                                strftime('%Y-%m-%d', InvoiceDate) AS date_value,
                                strftime('%d', InvoiceDate) AS day,
                                strftime('%m', InvoiceDate) AS month,
                                strftime('%Y', InvoiceDate) AS year
                           FROM invoice;
