import pandas as pd
excel_file_path = 'test.xlsx'
df = pd.read_excel(excel_file_path, sheet_name="Bot_Mapping")
var ='#'
print(df[df.eq(var).any(1)])

