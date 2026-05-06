INSERT INTO plant_types (type_name) VALUES
('Golden Pothos'),
('Bamboo'),
('Aloe Vera'),
('Monsterra'),
('Cactus'),
('Parlor Palm'),
('Nerve Plant'),
('Corn Plant'),
('Dracaena'),
('Palm');

INSERT INTO sizes (size_name) VALUES
('extra-small'),
('small'),
('medium'),
('large'),
('extra-large');

INSERT INTO locations (location_name) VALUES
('My room'),
('Living room');

INSERT INTO sunlight_levels (level) VALUES
('shade'),
('partial sun'),
('low sun'),
('full sun');

INSERT INTO watering_schedules (description) VALUES
('twice a week'),
('once a week'),
('once every 1.5 weeks'),
('once every 2 weeks'),
('once every 3 weeks');

INSERT INTO plants (name, age, type_id, size_id, location_id, sunlight_id)
VALUES 
('Coffee', '5+ years', 1, 5, 1, 1),
('Pinky', '2-3 years', 2, 3, 1, 3),
('Aloeha', '1.5 years', 3, 2, 1, 2),
('Terry-cota', '2 years', 4, 4, 1, 2),
('Teal Tale', '3 years', 1, 3, 2, 2),
('Greyt', '2 years', 4, 4, 2, 2),
('Prickles', '5 years', 5, 1, 1, 4),
('Blush Striped', 'unknown', 1, 3, 1, 1),
('Char-cole', 'unknown', 1, 3, 1, 2),
('Palmtastic', 'unknown', 10, 2, 1, 2),
('Silk Cloud', 'unknown', 9, 4, 1, 2),
('Cobalt', 'unknown', 7, 2, 2, 2);

INSERT INTO plant_watering (plant_id, schedule_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 1),
(5, 2),
(6, 2),
(7, 5),
(8, 1),
(9, 1),
(10, 3),
(11, 4),
(12, 3);