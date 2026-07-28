-- =====================================================
-- RAPIDO RIDE INTELLIGENCE SYSTEM
-- INSERT DATA
-- =====================================================

USE rapido_db;

-- -----------------------------------------------------
-- Data Import Method
-- -----------------------------------------------------
-- Dataset imported using:
-- MySQL Workbench → Table Data Import Wizard
--
-- Source File:
-- Dataset/Feature_Engineered/feature_engineered_rides.csv
--
-- Target Table:
-- rapido_rides
--
-- Imported Rows:
-- 50,000
-- -----------------------------------------------------

-- =====================================================
-- Verify Imported Data
-- =====================================================

SELECT COUNT(*) AS total_rows
FROM rapido_rides;

SELECT *
FROM rapido_rides
LIMIT 10;

-- =====================================================
-- Basic Validation
-- =====================================================

-- Total Revenue

SELECT SUM(total_fare) AS total_revenue
FROM rapido_rides;

-- Completed Rides

SELECT COUNT(*) AS completed_rides
FROM rapido_rides
WHERE ride_status='Completed';

-- Cancelled Rides

SELECT COUNT(*) AS cancelled_rides
FROM rapido_rides
WHERE ride_status='Cancelled';

-- Distinct Services

SELECT DISTINCT services
FROM rapido_rides;

-- Distinct Payment Methods

SELECT DISTINCT payment_method
FROM rapido_rides;