-- Script that lists all the records with a certain score in the second table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC