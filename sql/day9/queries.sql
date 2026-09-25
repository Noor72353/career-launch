-- Day 9 SQL Practice
-- JOINs, GROUP BY, Aggregations, HAVING, and Subqueries


-- 1. INNER JOIN: Show orders with customer names
SELECT
    orders.id AS order_id,
    users.name AS customer_name,
    orders.quantity,
    orders.order_date
FROM orders
INNER JOIN users
    ON orders.user_id = users.id;


-- 2. INNER JOIN: Show orders with product names
SELECT
    orders.id AS order_id,
    products.name AS product_name,
    orders.quantity,
    orders.order_date
FROM orders
INNER JOIN products
    ON orders.product_id = products.id;


-- 3. INNER JOIN: Show complete order information
SELECT
    orders.id AS order_id,
    users.name AS customer_name,
    products.name AS product_name,
    orders.quantity,
    products.price,
    orders.order_date
FROM orders
INNER JOIN users
    ON orders.user_id = users.id
INNER JOIN products
    ON orders.product_id = products.id;


-- 4. Calculate the total value of each order
SELECT
    orders.id AS order_id,
    users.name AS customer_name,
    products.name AS product_name,
    orders.quantity,
    products.price,
    orders.quantity * products.price AS total_value
FROM orders
INNER JOIN users
    ON orders.user_id = users.id
INNER JOIN products
    ON orders.product_id = products.id;


-- 5. LEFT JOIN: Show all users and their orders
SELECT
    users.name AS customer_name,
    orders.id AS order_id,
    orders.order_date
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id;


-- 6. GROUP BY: Count orders for each customer
SELECT
    users.name AS customer_name,
    COUNT(orders.id) AS order_count
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id
GROUP BY users.id, users.name;


-- 7. GROUP BY: Calculate total quantity ordered for each product
SELECT
    products.name AS product_name,
    SUM(orders.quantity) AS total_quantity
FROM products
INNER JOIN orders
    ON products.id = orders.product_id
GROUP BY products.id, products.name;


-- 8. GROUP BY: Calculate total revenue for each product
SELECT
    products.name AS product_name,
    SUM(orders.quantity * products.price) AS total_revenue
FROM products
INNER JOIN orders
    ON products.id = orders.product_id
GROUP BY products.id, products.name;


-- 9. GROUP BY: Calculate average product price by category
SELECT
    category,
    AVG(price) AS average_price
FROM products
GROUP BY category;


-- 10. GROUP BY + HAVING: Categories with average price above 10,000
SELECT
    category,
    AVG(price) AS average_price
FROM products
GROUP BY category
HAVING AVG(price) > 10000;


-- 11. GROUP BY + HAVING: Customers with more than one order
SELECT
    users.name AS customer_name,
    COUNT(orders.id) AS order_count
FROM users
INNER JOIN orders
    ON users.id = orders.user_id
GROUP BY users.id, users.name
HAVING COUNT(orders.id) > 1;


-- 12. Subquery: Products more expensive than the average product price
SELECT
    name,
    price
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);


-- 13. Subquery: Users who have placed at least one order
SELECT
    name
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
);


-- 14. Subquery: Most expensive product
SELECT
    name,
    price
FROM products
WHERE price = (
    SELECT MAX(price)
    FROM products
);


-- 15. TOP 3 CUSTOMERS BY TOTAL SPEND
SELECT
    users.name AS customer_name,
    SUM(orders.quantity * products.price) AS total_spend
FROM users
INNER JOIN orders
    ON users.id = orders.user_id
INNER JOIN products
    ON orders.product_id = products.id
GROUP BY users.id, users.name
ORDER BY total_spend DESC
LIMIT 3;

-- 16. RIGHT JOIN: Show all products and their orders
SELECT
    products.name AS product_name,
    orders.id AS order_id,
    orders.quantity
FROM orders
RIGHT JOIN products
    ON orders.product_id = products.id;