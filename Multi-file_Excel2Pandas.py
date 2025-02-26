# Converts excel files to pandas dataframes

import pandas as pd

# Paths for files to be converted
file_paths = ["path/file1.xlsx", "path/file2.xlsx"]
data_frames = []

# Converts the files to dataframes

for file_path, df in file_paths, data_frames:
	df = pd.read_excel(file_path)

# Prints the first 2 columns of the dataframes
for df in data_frames:
	print(df.iloc[:,0:2])


