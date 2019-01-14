import win32com.client

# Remove the protection from workbook
def remove_password_xlsx(filename, pw_str):
    xcl = win32com.client.Dispatch("Excel.Application")
    wb = xcl.Workbooks.Open(filename, False, False, None, pw_str)
    xcl.DisplayAlerts = False
    wb.SaveAs(filename, None, '', '')
    xcl.Quit()

    

import pandas as pd

# Stop Truncating Display of Dataframe in Jupyter
pd.options.display.max_rows = 4000
pd.options.display.max_columns = 4000


#Rename columns headers to the values in a row index
df2 = df.rename(columns=df.iloc[0])


# Count the missing values in a dataframe and display the data in a table
#https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe/39734251
def missing_values_table(df):
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        return mis_val_table_ren_columns
    
