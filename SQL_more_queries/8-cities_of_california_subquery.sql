-- Script that lists all cities of california that can be found in database
SELECT id, name
FROM cities
WHERE state_id = (
        SELECT Id
		FROM states
        WHERE name = 'California'
)
ORDER BY cities.id;