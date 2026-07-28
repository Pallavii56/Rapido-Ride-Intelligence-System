-- =========================================================
-- RAPIDO RIDE INTELLIGENCE SYSTEM
-- BUSINESS QUERIES
-- =========================================================

USE rapido_db;

-- =========================================================
-- SECTION 1 : OVERALL KPIs
-- =========================================================

--- Total Rides 
SELECT COUNT(*) AS Total_Rides
FROM rapido_rides;

--- Total Revenue 
SELECT
ROUND(SUM(total_fare),2) AS Total_Revenue
FROM rapido_rides;

--- Average Fare 
SELECT
ROUND(AVG(total_fare),2) AS Average_Fare
FROM rapido_rides;

--- Average Ride Distance 
SELECT
ROUND(AVG(distance),2) AS Average_Distance
FROM rapido_rides;

--- Average Ride Duration
SELECT
ROUND(AVG(duration),2) AS Average_Duration_Minutes
FROM rapido_rides;

--- Completed Rides 
SELECT COUNT(*) AS Completed_Rides
FROM rapido_rides
WHERE ride_status='Completed';

--- Cancelled Rides
SELECT COUNT(*) AS Cancelled_Rides
FROM rapido_rides
WHERE ride_status='Cancelled';

--- Cancellation Rate 
SELECT

ROUND(

SUM(Cancelled)/COUNT(*)*100

,2)

AS Cancellation_Percentage

FROM rapido_rides;

--- Total High Value Rides
SELECT COUNT(*) AS High_Value_Rides
FROM rapido_rides
WHERE High_Value_Ride=1;

--- Average Speed 
SELECT
ROUND(AVG(Average_Speed),2)
AS Average_Speed
FROM rapido_rides;

--- Service Analysis
SELECT

services,

COUNT(*) AS Total_Rides

FROM rapido_rides

GROUP BY services

ORDER BY Total_Rides DESC;

SELECT

services,

ROUND(SUM(total_fare),2) AS Revenue

FROM rapido_rides

GROUP BY services

ORDER BY Revenue DESC;

SELECT

services,

ROUND(AVG(total_fare),2) AS Average_Fare

FROM rapido_rides

GROUP BY services;

SELECT

services,

ROUND(AVG(distance),2) AS Average_Distance

FROM rapido_rides

GROUP BY services;

SELECT

services,

ROUND(AVG(duration),2) AS Average_Duration

FROM rapido_rides

GROUP BY services;

--- Time Analysis 

SELECT

Hour,

COUNT(*) AS Total_Rides

FROM rapido_rides

GROUP BY Hour

ORDER BY Hour;

SELECT

Hour,

ROUND(SUM(total_fare),2) Revenue

FROM rapido_rides

GROUP BY Hour

ORDER BY Revenue DESC;

SELECT

Weekday,

COUNT(*) AS Total_Rides

FROM rapido_rides

GROUP BY Weekday

ORDER BY Total_Rides DESC;

SELECT

Month,

ROUND(SUM(total_fare),2) Revenue

FROM rapido_rides

GROUP BY Month

ORDER BY Revenue DESC;

SELECT

Quarter,

ROUND(SUM(total_fare),2) Revenue

FROM rapido_rides

GROUP BY Quarter;

--- Location Analysis 

SELECT

source,

COUNT(*) AS Pickups

FROM rapido_rides

GROUP BY source

ORDER BY Pickups DESC

LIMIT 10;

SELECT

destination,

COUNT(*) AS Dropoffs

FROM rapido_rides

GROUP BY destination

ORDER BY Dropoffs DESC

LIMIT 10;

SELECT

source,

ROUND(SUM(total_fare),2) Revenue

FROM rapido_rides

GROUP BY source

ORDER BY Revenue DESC

LIMIT 10;

SELECT

destination,

ROUND(SUM(total_fare),2) Revenue

FROM rapido_rides

GROUP BY destination

ORDER BY Revenue DESC

LIMIT 10;

SELECT

source,

destination,

COUNT(*) AS Trips

FROM rapido_rides

GROUP BY source,destination

ORDER BY Trips DESC

LIMIT 10;

--- Payment Analysis 

SELECT

payment_method,

COUNT(*) Total_Rides

FROM rapido_rides

GROUP BY payment_method;

SELECT

payment_method,

ROUND(SUM(total_fare),2) Revenue

FROM rapido_rides

GROUP BY payment_method;


SELECT

payment_method,

ROUND(AVG(total_fare),2) Average_Fare

FROM rapido_rides

GROUP BY payment_method;

--- Business Insights 

SELECT

Time_Of_Day,

COUNT(*) AS Total_Rides

FROM rapido_rides

GROUP BY Time_Of_Day;

SELECT

Time_Of_Day,

ROUND(SUM(total_fare),2) Revenue

FROM rapido_rides

GROUP BY Time_Of_Day;

SELECT

Distance_Category,

COUNT(*) Total_Rides

FROM rapido_rides

GROUP BY Distance_Category;

SELECT

Fare_Category,

COUNT(*) Total_Rides

FROM rapido_rides

GROUP BY Fare_Category;

SELECT

Duration_Category,

COUNT(*) Total_Rides

FROM rapido_rides

GROUP BY Duration_Category;

SELECT

Peak_Hour,

COUNT(*) Total_Rides

FROM rapido_rides

GROUP BY Peak_Hour;

SELECT

Is_Weekend,

ROUND(SUM(total_fare),2) Revenue

FROM rapido_rides

GROUP BY Is_Weekend;

-----------------------------------------
-----------------------------------------
ADVANCED SQL
-----------------------------------------
-----------------------------------------

--- Top 10 Highest Fare Rides
SELECT *

FROM rapido_rides

ORDER BY total_fare DESC

LIMIT 10;

--- Top Revenue Services
SELECT

services,

SUM(total_fare) Revenue

FROM rapido_rides

GROUP BY services

ORDER BY Revenue DESC;

--- Rank Services by Revenue
SELECT

services,

SUM(total_fare) Revenue,

RANK() OVER(

ORDER BY SUM(total_fare) DESC

) AS Service_Rank

FROM rapido_rides

GROUP BY services;

--- Monthly Running Revenue
SELECT

Month,

SUM(total_fare) Revenue,

SUM(SUM(total_fare))

OVER(

ORDER BY Month_Number

) Running_Revenue

FROM rapido_rides

GROUP BY Month,Month_Number;

--- Top 5 Pickup Locations
SELECT

source,

COUNT(*) Total_Rides

FROM rapido_rides

GROUP BY source

ORDER BY Total_Rides DESC

LIMIT 5;
