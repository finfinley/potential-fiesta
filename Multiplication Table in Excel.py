#! python3
# Automate the Boring Stuff // Practice Project // Multiplication Table Maker

import openpyxl, sys
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font


# User usage 
if len(sys.argv) < 2:
	print('Usage: python multiplicationTable.py [number] - Creates an excel file with desired multiplication table')
	print(sys.executable)
	print(sys.version)
	print(sys.path)
	sys.exit()

# Gets user input from command line 
n = sys.argv[1]
n = int(n)

# Opens Workbook
wb = openpyxl.Workbook()
sheet = wb['Sheet']

# Font style for labels 
bold_font = Font(bold = True)

# Creates labels for rows and columns 
for number in range(1, n+1):
	sheet[get_column_letter(number+1) + '1'] = number
	sheet['A' + str(number+1)] = number
	# Styles the labels as bold 
	sheet['A' + str(number+1)].font=bold_font
	sheet[get_column_letter(number+1) + '1'].font = bold_font


# Creates multiplication table
for row in range(sheet.min_column, sheet.max_row):
	for col in range(sheet.min_column, sheet.max_row):
			sheet[get_column_letter(row+1) + str(col+1)] = row * col

print('Workbook created.')
wb.save('{}multiplicationtable.xlsx'.format(n))
