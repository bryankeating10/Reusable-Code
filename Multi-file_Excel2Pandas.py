# Converts excel files to pandas dataframes
import pandas as pd
import os

# Paths for files to be converted (using raw strings to avoid unicode errors)
file_paths = [r"path_one", r"path_two", r"path_three"]
data_frames = []

# Convert the files to dataframes
for file_path in file_paths:
	df = pd.read_excel(file_path)
	# Prints the title of the excel file that was converted
	print(f'{os.path.basename(file_path)} converted to a dataframe')
	data_frames.append(df)