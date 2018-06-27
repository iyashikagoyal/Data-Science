CREATE TABLE Dim_Track AS SELECT t.TrackId as dim_track_id,
                                 t.Name as track_name,
                                 al.Title as album_name,
                                 ar.Name as artist_name,
                                 t.Composer as composer,
                                 g.Name as genre,
                                 m.Name as mediatype
                            FROM Album AS al
                                 JOIN
                                 Artist AS ar ON al.ArtistId = ar.ArtistId
                                 JOIN
                                 Track AS t ON al.AlbumId = t.AlbumId
                                 JOIN
                                 MediaType AS m ON m.MediaTypeId = t.MediaTypeId
                                 JOIN
                                 Genre AS g ON t.GenreId = g.GenreId;
