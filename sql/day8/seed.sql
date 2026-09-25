INSERT INTO users (id, name, email, city) VALUES
(1, 'Ali Khan', 'ali@example.com', 'Islamabad'),
(2, 'Sara Ahmed', 'sara@example.com', 'Rawalpindi'),
(3, 'Hamza Malik', 'hamza@example.com', 'Lahore'),
(4, 'Ayesha Noor', 'ayesha@example.com', 'Karachi'),
(5, 'Usman Shah', 'usman@example.com', 'Peshawar'),
(6, 'Fatima Khan', 'fatima@example.com', 'Islamabad');

INSERT INTO products (id, name, category, price) VALUES
(1, 'Laptop', 'Electronics', 120000),
(2, 'Keyboard', 'Electronics', 5000),
(3, 'Mouse', 'Electronics', 2500),
(4, 'Office Chair', 'Furniture', 25000),
(5, 'Desk', 'Furniture', 30000),
(6, 'Notebook', 'Stationery', 500),
(7, 'Headphones', 'Electronics', 8000);

INSERT INTO orders (id, user_id, product_id, quantity, order_date) VALUES
(1, 1, 1, 1, '2026-09-01'),
(2, 2, 2, 2, '2026-09-02'),
(3, 3, 3, 1, '2026-09-03'),
(4, 1, 4, 1, '2026-09-04'),
(5, 4, 5, 1, '2026-09-05'),
(6, 5, 6, 5, '2026-09-06'),
(7, 2, 7, 1, '2026-09-07'),
(8, 6, 2, 1, '2026-09-08'),
(9, 3, 6, 3, '2026-09-09'),
(10, 4, 3, 2, '2026-09-10');