import pandas as pd
filename = 'an_excel_file.xlsx'

xl = pd.ExcelFile(filename)
exists = True if 'Budget Summary' in xl.sheet_names else False  #xl.sheet_names returns a list of sheet names
