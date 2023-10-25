SELECT AVG(rating) FROM movies JOIN ratings ON movies.id = ratings.movies_id WHERE year = 2012;
