-- Switch to the correct database
USE alx_book_store;

-- -------------------------------------------------------------------
-- 1. Table: Authors
-- Stores information about authors.
-- Contains AUTHOR_ID (PK) and AUTHOR_NAME.
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Authors (
    AUTHOR_ID INT PRIMARY KEY,
    AUTHOR_NAME VARCHAR(215) NOT NULL
);

-- -------------------------------------------------------------------
-- 2. Table: Books
-- Stores information about books available in the bookstore.
-- References Authors(AUTHOR_ID)
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Books (
    BOOK_ID INT PRIMARY KEY,
    TITLE VARCHAR(130) NOT NULL,
    AUTHOR_ID INT,
    PRICE DOUBLE NOT NULL,
    PUBLICATION_DATE DATE,
    FOREIGN KEY (AUTHOR_ID) REFERENCES Authors(AUTHOR_ID)
);

-- -------------------------------------------------------------------
-- 3. Table: Customers
-- Stores information about customers.
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Customers (
    CUSTOMER_ID INT PRIMARY KEY,
    CUSTOMER_NAME VARCHAR(215) NOT NULL,
    EMAIL VARCHAR(215) NOT NULL UNIQUE,
    ADDRESS TEXT
);

-- -------------------------------------------------------------------
-- 4. Table: Orders
-- Stores information about orders placed by customers.
-- References Customers(CUSTOMER_ID)
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Orders (
    ORDER_ID INT PRIMARY KEY,
    CUSTOMER_ID INT,
    ORDER_DATE DATE NOT NULL,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES Customers(CUSTOMER_ID)
);

-- -------------------------------------------------------------------
-- 5. Table: Order_Details
-- Stores information about the books included in each order.
-- References Orders(ORDER_ID) and Books(BOOK_ID)
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Order_Details (
    ORDERDETAILID INT PRIMARY KEY,
    ORDER_ID INT,
    BOOK_ID INT,
    QUANTITY DOUBLE NOT NULL,
    FOREIGN KEY (ORDER_ID) REFERENCES Orders(ORDER_ID),
    FOREIGN KEY (BOOK_ID) REFERENCES Books(BOOK_ID)
);
