SELECT dt.artist_name as Artist,
       dd.year as Year,
       dl.city as City,
       count(dt.dim_track_id) as TotalTracksSold
  FROM Fact_Sale AS fs
       JOIN
       Dim_Track AS dt ON fs.dim_track_id = dt.dim_track_id
       JOIN
       Dim_Date AS dd ON fs.dim_date_id = dd.dim_date_id
       JOIN
       Dim_Location AS dl ON fs.dim_location_id = dl.dim_location_id
 GROUP BY dt.artist_name,
          dd.year,
          dl.city;