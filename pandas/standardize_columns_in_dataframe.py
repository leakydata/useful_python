import pandas as pd
from sklearn.preprocessing import StandardScaler

df[[x for x in df.columns.tolist()]] = StandardScaler().fit_transform(df[[x for x in df.columns.tolist()]])

#Create a new numerical data only dataframe
df_std = pd.DataFrame(df, columns = [x for x in df.columns.tolist()])
