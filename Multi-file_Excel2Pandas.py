import pandas as pd

file_paths = []
data_frames = []

for file_path in file_paths:
	df = pd.read_excel(file_path)
	data_frames.append(df)