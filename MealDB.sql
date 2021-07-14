-- To Fetch the information from MealDB

SELECT * FROM MealDB;

-- To select a row from table

SELECT * FROM MealDB limit 1;

-- To select limited rows from table

SELECT * FROM MealDB limit 5;

-- Delete

DELETE from MealDB WHERE meal_id = 1438;

SELECT * FROM MealDB WHERE meal_id = 1438;


-- Update the record of mealdb based on the condition

UPDATE MealDB SET category = "Salad" WHERE meal_id = 2307;

SELECT * FROM MealDB;

-- Insert records into mealdb

INSERT into MealDB values(1755, "Beverages", "Thai");

SELECT * FROM MealDB;

-- Drop a table

Drop table MealDB;

-- Sort in order
SELECT * FROM MealDB ORDER BY Pizza DESC;
