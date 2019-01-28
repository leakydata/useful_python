#Remove new line (\n) characters from the entire dataframe
df = df.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)

#Filter out different criteria like: Type = S, iQ is not Nan, and rows/cells that are all uppercase
new_df = df[(df.Type == 'S') & (df.Product.isna()) & (df.QUESTION.str.isupper())]

#Drop any rows that contain any/a single empty/NaN value (axis = 1 for columns)
df = df.dropna(axis=0, how='any')

#Drop any rows that are all empty/NaN values (axis = 1 for columns)
df = df.dropna(axis=0, how='all')
