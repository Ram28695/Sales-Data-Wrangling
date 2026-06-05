# Sales Dataset Wrangling Project

##  Objective
This project focuses on cleaning and preparing a sales dataset for analysis.  
The goal is to remove inconsistencies, handle missing values, standardize formats, and document the dataset with a data dictionary.

##  Files in this Repository
- **Sales_Dataset.csv** → Raw dataset
- **Sales_Dataset_Cleaned.csv** → Cleaned dataset after wrangling
- **Data_Dictionary.xlsx** → Documentation of columns, data types, and descriptions
- **prep1.py** → Python script used for cleaning
- **README.md** → Project summary and instructions

##  Steps Performed
1. **Removed duplicates** to ensure unique records.
2. **Handled missing values**:
   - Numeric columns → filled with median
   - Text columns → filled with mode or `"Unknown"`
3. **Standardized column names** (lowercase, underscores).
4. **Cleaned text columns** (stripped spaces, converted to lowercase).
5. **Removed outliers** using the IQR method.
6. **Saved cleaned dataset** for further analysis.

##  Data Dictionary (Summary)
| Column Name   | Data Type | Description |
|---------------|-----------|-------------|
| order_id      | object    | Unique identifier for each order |
| amount        | int64     | Total monetary value of the order |
| profit        | int64     | Net profit earned from the order |
| quantity      | int64     | Number of units purchased |
| category      | object    | Broad classification of product |
| sub_category  | object    | Specific classification within category |
| paymentmode   | object    | Customer payment method |
| order_date    | object    | Date when the order was placed |
| customername  | object    | Name of the customer |
| state         | object    | State where order was delivered |
| city          | object    | City where order was delivered |
| year_month    | object    | Year and month derived from order date |

##  How to Run
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install pandas numpy
