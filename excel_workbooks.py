import win32com.client

#Remove the protection from workbook
def remove_password_xlsx(filename, pw_str):
    xcl = win32com.client.Dispatch("Excel.Application")
    wb = xcl.Workbooks.Open(filename, False, False, None, pw_str)
    xcl.DisplayAlerts = False
    wb.SaveAs(filename, None, '', '')
    xcl.Quit()

    

import pandas as pd

#Stop truncating printed results
pd.options.display.max_rows = 4000
pd.options.display.max_columns = 4000
