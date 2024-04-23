import itertools
import xlrd
import xlsxwriter
import numpy as np

# Open the Excel workbook
workbook = xlrd.open_workbook('data.xlsx', on_demand=True)

# Get the first worksheet in the workbook
worksheet = workbook.sheet_by_index(0)

first_row = [worksheet.cell_value(0, col) for col in range(worksheet.ncols)]
# Print the column headers
print(first_row)

# Transform the workbook into a list of dictionaries
data = []
for row in range(1, worksheet.nrows):
    row_data = {
        first_row[col]: worksheet.cell_value(row, col)
        for col in range(worksheet.ncols)
    }
    data.append(row_data)

# Mengambil nilai dari Excel ke ras_alice
ras_alice = []
for row in range(1, worksheet.nrows):
    elm = [worksheet.cell_value(row, col) for col in range(1)]
    ras_alice.append(elm)

# Mengambil nilai dari Excel ke ras_bob
ras_bob = []
for row in range(1, worksheet.nrows):
    elm = [worksheet.cell_value(row, col) for col in range(2)]
    ras_bob.append([int(x) for x in elm])
