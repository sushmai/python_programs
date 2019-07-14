#!/usr/bin/env python
# To read and write from excel import openpyxl
import openpyxl
# to read an write csv files 
# unicodecsv helps when working with utf-8 characters 
import unicodecsv
#-----------------
# Opening a file and make sure it's existing 
#-----------------

try:
    #open work book, and make sure the type of file
    #helpful when submitting file as argument 
    wb = openpyxl.load_workbook("hire.xlsx")
    print(type(wb))
    sh = wb.get_active_sheet()

    #convert file to CSV
    with open('hire1.csv', 'wb') as f:
        c = unicodecsv.writer(f)
        for r in sh.rows:
            c.writerow([cell.value for cell in r])
            
except IOError as e:
    print(" The file is not present")
