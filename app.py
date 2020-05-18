import pandas as pd
import openpyxl as xl
from converter import rows

# Here at line 6 is given the location, which file will be converted
read_file = pd.read_csv(r"C:\Users\lenovo\Desktop\05-08-2020.csv")

# Here this line is given the location where the file will be converted.
read_file.to_excel(r"G:\Python\Hello world by pycharm.xlsx", index=None, header=True)

# Here is loading the file at at workbook
wb = xl.load_workbook(r"G:\Python\Hello world by pycharm.xlsx")

# Crete a new sheet
ws = wb.create_sheet("Sheet2")

# importing Data from another a sub file and uploading on the new sheet
for row in rows:
    ws.append(row)

# Save the file
wb.save("Co.xlsx")


