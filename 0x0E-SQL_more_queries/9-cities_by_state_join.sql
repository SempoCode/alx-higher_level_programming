-- List all cities and their state names in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name 
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
