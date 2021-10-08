import openpyxl
import os

wb = openpyxl.Workbook()
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'].value
sheet['A2'] = 'Hello'

os.chdir('c:\\Users\\All\\Documents')
wb.save('example.xlsx')