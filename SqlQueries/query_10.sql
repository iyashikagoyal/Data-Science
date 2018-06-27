SELECT ar.Name AS ArtistName,
       COUNT(DISTINCT t.TrackId) AS NoOfTracks,
       COUNT(DISTINCT pt.PlaylistId) AS NoOfPlaylists
  FROM Album AS al
       JOIN
       Artist AS ar ON al.ArtistId = ar.ArtistId
       JOIN
       Track AS t ON al.AlbumId = t.AlbumId
       JOIN
       PlaylistTrack AS pt ON t.TrackId = pt.TrackId
 GROUP BY ar.ArtistId
HAVING COUNT(DISTINCT pt.PlaylistId) >= 6
 ORDER BY COUNT(DISTINCT t.TrackId) DESC;
