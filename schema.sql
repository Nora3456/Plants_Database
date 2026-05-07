CREATE DATABASE IF NOT EXISTS plant_db;
USE plant_db;

-- Plant types
CREATE TABLE plant_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE
);

-- Sizes
CREATE TABLE sizes (
    size_id INT AUTO_INCREMENT PRIMARY KEY,
    size_name VARCHAR(20) NOT NULL UNIQUE
);

-- location
CREATE TABLE locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(50) NOT NULL UNIQUE
);

-- sunlight amounts
CREATE TABLE sunlight_levels (
    sunlight_id INT AUTO_INCREMENT PRIMARY KEY,
    level VARCHAR(50) NOT NULL UNIQUE
);

-- watering schedules
CREATE TABLE watering_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(100) NOT NULL UNIQUE
);

-- main plants table
CREATE TABLE plants (
    plant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age VARCHAR(50),

    type_id INT NOT NULL,
    size_id INT NOT NULL,
    location_id INT NOT NULL,
    sunlight_id INT NOT NULL,

    FOREIGN KEY (type_id) REFERENCES plant_types(type_id)
        ON DELETE CASCADE,

    FOREIGN KEY (size_id) REFERENCES sizes(size_id),

    FOREIGN KEY (location_id) REFERENCES locations(location_id),

    FOREIGN KEY (sunlight_id) REFERENCES sunlight_levels(sunlight_id),

    CHECK (name <> '')
);
