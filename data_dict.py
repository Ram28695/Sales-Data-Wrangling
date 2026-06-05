import pandas as pd

# Build the data dictionary
data_dict = pd.DataFrame({
    "Column Name": [
        "Order ID", "Amount", "Profit", "Quantity", "Category",
        "Sub-Category", "PaymentMode", "Order Date", "CustomerName",
        "State", "City", "Year-Month"
    ],
    "Data Type": [
        "object", "int64", "int64", "int64", "object",
        "object", "object", "object", "object",
        "object", "object", "object"
    ],
    "Description": [
        "Unique identifier for each order",
        "Total monetary value of the order",
        "Net profit earned from the order",
        "Number of units purchased",
        "Broad classification of product",
        "Specific classification within category",
        "Customer payment method",
        "Date when the order was placed",
        "Name of the customer",
        "State where order was delivered",
        "City where order was delivered",
        "Year and month derived from order date"
    ]
})

# Save to Excel
data_dict.to_excel(r"C:\Users\Karthik\OneDrive\Documents\Analytics_Project\Data_Dictionary.xlsx", index=False)
print("Data dictionary saved to Data_Dictionary.xlsx")
