# https://stackoverflow.com/questions/25788037/pandas-df-to-csvfile-csv-encode-utf-8-still-gives-trash-characters-for-min
df.to_csv("df.csv",index=0, encoding='utf-8-sig') #using utf-8 or sys.getfilesystemencoding() still produced garbage but adding sig fixed it
