-- alx_book_store.sql

-- Database Creation
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- Table: Authors
-- Stores information about authors.
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- Table: Books
-- Stores information about books available in the bookstore.
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Table: Customers
-- Stores information about customers.
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL UNIQUE, -- Assuming email should be unique for each customer
    address TEXT
);

-- Table: Orders
-- Stores information about orders placed by customers.
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Table: Order_Details
-- Stores information about the books included in each order.
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
    -- Consider adding a UNIQUE constraint on (order_id, book_id) to prevent duplicate books in an order
);
