import pandas as pd

file_path = ''				# Replace with the path to the Excel file
excel_file = pd.ExcelFile(file_path)
data_frames = []

for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    data_frames.append(df)
