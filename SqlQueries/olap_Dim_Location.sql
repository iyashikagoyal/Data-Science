CREATE TABLE IF NOT EXISTS Dim_Location AS SELECT CustomerId AS dim_location_id,
                                                  City AS city,
                                                  State AS state,
                                                  Country AS country,
                                                  Postalcode AS postalcode
                                             FROM Customer;
