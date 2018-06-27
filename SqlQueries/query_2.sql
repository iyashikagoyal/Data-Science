SELECT a.Title as AlbumName,
       t.Name as TrackName,
       MAX(t.Milliseconds) as Milliseconds
  FROM Album AS a
       JOIN
       Track AS t ON a.AlbumId = t.AlbumId;