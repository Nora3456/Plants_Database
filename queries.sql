-- View all plants
SELECT * FROM plants;

-- Views plants with the full detail"
SELECT 
    p.name,
    p.age,
    t.type_name,
    s.size_name,
    l.location_name,
    sl.level
FROM plants p
JOIN plant_types t ON p.type_id = t.type_id
JOIN sizes s ON p.size_id = s.size_id
JOIN locations l ON p.location_id = l.location_id
JOIN sunlight_levels sl ON p.sunlight_id = sl.sunlight_id;

-- Shows plants by location
SELECT name
FROM plants
WHERE location_id = 1;

-- Shows plants that need partial sun
SELECT p.name, sl.level
FROM plants p
JOIN sunlight_levels sl ON p.sunlight_id = sl.sunlight_id
WHERE sl.level = 'partial sun';

-- Counts plants per loaction
SELECT l.location_name, COUNT(*) AS total_plants
FROM plants p
JOIN locations l ON p.location_id = l.location_id
GROUP BY l.location_name;

-- Finds all the large plants
SELECT p.name, s.size_name
FROM plants p
JOIN sizes s ON p.size_id = s.size_id
WHERE s.size_name = 'Large';

-- Shows plants with watering schedules
SELECT 
    p.name,
    ws.schedule_name
FROM plants p
JOIN plant_watering pw ON p.plant_id = pw.plant_id
JOIN watering_schedules ws ON pw.schedule_id = ws.schedule_id;

-- Shows plants grouped by their typew
SELECT t.type_name, COUNT(*) AS total
FROM plants p
JOIN plant_types t ON p.type_id = t.type_id
GROUP BY t.type_name;