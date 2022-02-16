import pandas as pd
from sklearn.preprocessing import StandardScaler

df[[x for x in df.columns.tolist()]] = StandardScaler().fit_transform(df[[x for x in df.columns.tolist()]])
