SELECT art.Name AS Artist,
       alb.Title
  FROM Artist AS art
       JOIN
       Album AS alb ON art.ArtistId = alb.ArtistId
 WHERE art.Name LIKE 'U%'
 GROUP BY art.Name,
          alb.Title;