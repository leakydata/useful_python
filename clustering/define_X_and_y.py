# define datasets
X = df_std[[x for x in df_std.columns.tolist()]].to_numpy()
y = df_std['PREDICTED_VARIABLE'].to_numpy()
