import xlrd #ライブラリのインポート
import pandas as pd
input_file_name = 'since2003_visitor_arrivals.xlsx'
input_book = pd.ExcelFile(input_file_name)
input_sheet_name = input_book.sheet_names
num_sheet = len(input_sheet_name)
print("sheetの数:", num_sheet)
print(input_sheet_name)