import pandas as pd

# Load CSV file
csv_data = pd.read_csv("C:\\Users\\ACER\\OneDrive\\Desktop\\MyProject\\Dataset\\Students.csv")

# Load Excel file
#excel_data = pd.read_excel("data/customers.xlsx")

print("CSV Data Preview:")
print(csv_data.head())
print(csv_data.tail())

#print("\nExcel Data Preview:")
#print(excel_data.head())
