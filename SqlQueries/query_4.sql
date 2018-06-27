SELECT art.Name AS ArtistName,
       alb.Title AS AlbumTitle,
       COUNT(t.TrackId) AS NoofTracks
  FROM Album AS alb
       JOIN
       Track AS t ON alb.AlbumId = t.AlbumId
       JOIN
       Artist AS art ON art.ArtistId = alb.ArtistId
 GROUP BY alb.Title
 ORDER BY COUNT(t.TrackId) DESC
 LIMIT 10;