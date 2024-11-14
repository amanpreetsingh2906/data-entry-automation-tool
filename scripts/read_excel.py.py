import pandas as pd

# Load the Excel file
file_path = r"C:\Users\LENOVO\Documents\GitHub\data-entry-automation-tool\data\sampledataworkorders.xlsx"
data = pd.read_excel(file_path)
print("Data from excel file: ")
print(data)
