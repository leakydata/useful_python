# Remove Column Heading Formatting In Excel Export
#pd.io.formats.excel.ExcelFormatter.header_style = None
from pandas.io.formats import excel
excel.ExcelFormatter.header_style = None

# Pandas Nans to None
df = df.replace([np.nan], [None])
df = df.where(pd.notnull(df), None)

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

# Iterate through two columns as key value pairs
for k, v in df.itertuples(index=False):
    print(k,v)

# Convert two columns into key and value pairs in a newly defined dict
new_dict = dict(zip(df.Column1, df.Column2))

#Select rows that contain int digits only
df[df['column_name'].astype(str).str.isdigit()]


#########################################################
#     This section cleans up the workbook/dataframe     #
#########################################################

# Remove all newline characters from the dataframe
df = df.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)

# Find the row containing a string that is supposed to be a header and copy that row to the column names and remove the row
def fix_headers(df,identifying_string):
    mask = np.column_stack([df[col].astype(str).str.contains(r"%s"%identifying_string, na=False) for col in df])
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
        
#Slightly simpler drop exes        
def drop_exes(df):
    location = df[df[df.columns[0]].str.contains(r"xxxxxxxx.*", na=False) == True]
    if len(location) >= 1:
        location = location.index[0]
        df.drop(df.index[location], inplace=True)
        
# Reset the dataframe index and drop the old index to prevent it from possibly being added as a new column
df.reset_index(drop=True)


# Pandas/Numpy rounds 0.5 (halves) to the nearest even integer so I can't round whole dataframe without losing values to round truncation: this fixes that issue
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def round_1(x):
    return(round_half_up(float(x),1))

def round_2(x):
    return(round_half_up(float(x),2))


##########################################
# CONVERTING DATAFRAMES TO OTHER OBJECTS #
##########################################

#converts a dataframe to list of dictionaries / each row is a dict
df.to_dict(orient='records') 

#Convert the dataframe to a csv and fix character encoding for excel and drop index so it doesn't end up in the csv
df.to_csv('file.csv',encoding='utf-8-sig')
