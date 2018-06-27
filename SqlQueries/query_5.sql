SELECT ArtistId,
       Name AS ArtistName
  FROM Artist
 WHERE NOT EXISTS (
               SELECT ArtistId
                 FROM Album
                WHERE Artist.ArtistId = Album.ArtistId
           );