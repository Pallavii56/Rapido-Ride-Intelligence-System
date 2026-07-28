-- =====================================================
-- RAPIDO RIDE INTELLIGENCE SYSTEM
-- CREATE DATABASE & TABLE
-- =====================================================

-- Create Database
CREATE DATABASE IF NOT EXISTS rapido_db;

-- Use Database
USE rapido_db;

-- Drop table if already exists
DROP TABLE IF EXISTS rapido_rides;

-- =====================================================
-- Create Main Table
-- =====================================================

CREATE TABLE rapido_rides (

    -- Original Dataset Columns
    ride_id VARCHAR(50) PRIMARY KEY,
    services VARCHAR(50),
    date DATE,
    time TIME,
    ride_status VARCHAR(30),
    source VARCHAR(100),
    destination VARCHAR(100),
    duration INT,
    distance FLOAT,
    ride_charge DECIMAL(10,2),
    misc_charge DECIMAL(10,2),
    total_fare DECIMAL(10,2),
    payment_method VARCHAR(50),

    -- Date Features
    Year INT,
    Month VARCHAR(20),
    Month_Number INT,
    Quarter INT,
    Day INT,
    Weekday VARCHAR(20),
    Week_Number INT,

    -- Time Features
    Hour INT,
    Minute INT,
    Second INT,
    Time_Of_Day VARCHAR(20),

    -- Business Features
    Peak_Hour BOOLEAN,
    Is_Weekend BOOLEAN,

    Ride_Revenue DECIMAL(10,2),

    Distance_Category VARCHAR(30),
    Duration_Category VARCHAR(30),
    Fare_Category VARCHAR(30),

    Fare_Per_KM FLOAT,
    Average_Speed FLOAT,

    High_Value_Ride BOOLEAN,
    Cancelled BOOLEAN,
    Completed BOOLEAN

);

-- =====================================================
-- Verify Table
-- =====================================================

SHOW TABLES;

DESCRIBE rapido_rides;