from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Select the active worksheet
sheet = wb.active

# Write data to cells
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'

# Sample data
data = [
    ('keerthana', 23),
    ('abinaya', 25),
    ('kavya', 21),
    ('Aarthika', 26)
]

# Write data from list of tuples
for row_index, (name, age) in enumerate(data, start=2):
    sheet[f'A{row_index}'] = name
    sheet[f'B{row_index}'] = age

# Save the workbook with a specific filename
output_filename = 'keerthana.xlsx'
wb.save(output_filename)
