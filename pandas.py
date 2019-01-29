#Remove new line (\n) characters from the entire dataframe
df = df.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)

#Filter out different criteria like: Type = S, iQ is not Nan, and rows/cells that are all uppercase
new_df = df[(df.Type == 'S') & (df.Product.isna()) & (df.QUESTION.str.isupper())]

#Drop any rows that contain any/a single empty/NaN value (axis = 1 for columns)
df = df.dropna(axis=0, how='any')

#Drop any rows that are all empty/NaN values (axis = 1 for columns)
df = df.dropna(axis=0, how='all')

# Create new row and set value based on value in other column or series
df['answer_type'] = np.where((df['numeric_answer'] != 'nan'), 1, 0)

#Find rows that contain a string or part of string and set value of new row to 1
df['reps_only'] = np.where((df['question'].str.contains("Rep's ONLY", flags=re.IGNORECASE, regex=True)), 'rep', 0)

#########################################################
#     This section cleans up the workbook/dataframe     #
#########################################################

# Remove all newline characters from the dataframe
df = df.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)

# Find the row containing a string that is supposed to be a header and copy that row to the column names and remove the row
def fix_headers(df,identifying_string):
    mask = np.column_stack([df[col].str.contains(r"%s"%identifying_string, na=False) for col in df])
    if len(df.loc[mask.any(axis=1)].index) >= 1:
        row_location = df.loc[mask.any(axis=1)].index[0]
        df.rename(columns=df.iloc[row_location], inplace=True)
        df.drop(df.index[row_location], inplace=True)

# Remove any row containing the letter 'x' repeated more than 6 times    
def drop_exes(df):
    mask = np.column_stack([df[col].str.contains(r"xxxxxxx.*", na=False) for col in df])
    if len(df.loc[mask.any(axis=1)].index) >= 1:
        location = df.loc[mask.any(axis=1)].index[0]
        df.drop(df.index[location], inplace=True)

# Reset the dataframe index and drop the old index to prevent it from possibly being added as a new column
df.reset_index(drop=True)

