import numpy as np

# select the float columns and in columns
df_num = df.select_dtypes(include=[np.float,np.int])
