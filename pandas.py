#Remove new line (\n) characters from the entire dataframe
df = df.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)

#Filter out different criteria like: Type = S, iQ is not Nan, and rows/cells that are all uppercase
new_df = df[(df.Type == 'S') & (df.Product.isna()) & (df.QUESTION.str.isupper())]
