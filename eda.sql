

CREATE TABLE sales_data (
    order_id VARCHAR(50),
    amount DECIMAL(10,2),
    profit DECIMAL(10,2),
    quantity INT,
    category VARCHAR(50),
    sub_category VARCHAR(50),
    paymentmode VARCHAR(50),
    order_date DATE,
    customername VARCHAR(100),
    state VARCHAR(50),
    city VARCHAR(50),
    year_month VARCHAR(20)
);

CREATE OR REPLACE DIRECTORY data_dir AS 'C:/Users/Karthik/OneDrive/Documents/Analytics_Project';
GRANT READ, WRITE ON DIRECTORY data_dir TO sales_project;

CREATE TABLE sales_data_ext (
    order_id VARCHAR2(50),
    amount NUMBER,
    profit NUMBER,
    quantity NUMBER,
    category VARCHAR2(50),
    sub_category VARCHAR2(50),
    paymentmode VARCHAR2(50),
    order_date DATE,
    customername VARCHAR2(100),
    state VARCHAR2(50),
    city VARCHAR2(50),
    year_month VARCHAR2(20)
)
ORGANIZATION EXTERNAL (
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY data_dir
    ACCESS PARAMETERS (
        RECORDS DELIMITED BY NEWLINE
        FIELDS TERMINATED BY ','
        MISSING FIELD VALUES ARE NULL
    )
    LOCATION ('Sales_Dataset_Cleaned.csv')
)
REJECT LIMIT UNLIMITED;

INSERT INTO sales_data SELECT * FROM sales_data_ext;

SELECT category, SUM(amount) AS TotalSales
FROM sales_data
GROUP BY category
ORDER BY TotalSales DESC;

SELECT TO_CHAR(order_date, 'YYYY-MM') AS Month,
       SUM(amount) AS TotalSales
FROM sales_data
GROUP BY TO_CHAR(order_date, 'YYYY-MM')
ORDER BY Month;

SELECT customername,
       SUM(amount) AS TotalSpent
FROM sales_data
GROUP BY customername
ORDER BY TotalSpent DESC
FETCH FIRST 5 ROWS ONLY;

SELECT state, AVG(amount) AS AvgOrderValue
FROM sales_data
GROUP BY state
ORDER BY AvgOrderValue DESC;
