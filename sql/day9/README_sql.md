\# SQL Database Documentation



\## Overview



This project uses SQLite to practice SQL fundamentals, JOINs, aggregations,

GROUP BY, HAVING, and subqueries.



The database is stored in:



`practice.db`



\## Database Schema



The database contains three tables:



\### 1. users



Stores customer information.



| Column | Type | Description |

|---|---|---|

| id | INTEGER | Primary key |

| name | TEXT | Customer name |

| email | TEXT | Customer email |

| city | TEXT | Customer city |



\### 2. products



Stores product information.



| Column | Type | Description |

|---|---|---|

| id | INTEGER | Primary key |

| name | TEXT | Product name |

| category | TEXT | Product category |

| price | REAL | Product price |



\### 3. orders



Stores customer orders.



| Column | Type | Description |

|---|---|---|

| id | INTEGER | Primary key |

| user\_id | INTEGER | References `users.id` |

| product\_id | INTEGER | References `products.id` |

| quantity | INTEGER | Number of products ordered |

| order\_date | TEXT | Date of the order |



\## Relationships



The tables are related as follows:



```text

users

&#x20; |

&#x20; | 1-to-many

&#x20; v

orders

&#x20; |

&#x20; | many-to-1

&#x20; v

products

