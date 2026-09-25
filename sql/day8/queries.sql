-- Day 8 SQL Practice
-- SQL Fundamentals: SELECT, WHERE, LIKE, ORDER BY, LIMIT

-- 1. Select all users
SELECT *
FROM users;

-- 2. Select specific user columns
SELECT name, email
FROM users;

-- 3. Find users from Islamabad
SELECT *
FROM users
WHERE city = 'Islamabad';

-- 4. Find users whose name contains "a"
SELECT *
FROM users
WHERE name LIKE '%a%';

-- 5. Find products costing more than 10,000
SELECT *
FROM products
WHERE price > 10000;

-- 6. Find products in the Electronics category
SELECT *
FROM products
WHERE category = 'Electronics';

-- 7. Find products priced between 2,000 and 30,000
SELECT *
FROM products
WHERE price BETWEEN 2000 AND 30000;

-- 8. Find products whose name contains "o"
SELECT *
FROM products
WHERE name LIKE '%o%';

-- 9. Sort products by price from lowest to highest
SELECT *
FROM products
ORDER BY price ASC;

-- 10. Sort products by price from highest to lowest
SELECT *
FROM products
ORDER BY price DESC;

-- 11. Show the 3 most expensive products
SELECT *
FROM products
ORDER BY price DESC
LIMIT 3;

-- 12. Show the 3 cheapest products
SELECT *
FROM products
ORDER BY price ASC
LIMIT 3;

-- 13. Find orders placed by user 1
SELECT *
FROM orders
WHERE user_id = 1;

-- 14. Find orders with quantity greater than 1
SELECT *
FROM orders
WHERE quantity > 1;

-- 15. Show the latest 5 orders
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 5;