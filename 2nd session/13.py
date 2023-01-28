#How would you write a pandas DataFrame to an Excel file in Python



import pandas as pd
import openpyxl

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

print(df)
df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')