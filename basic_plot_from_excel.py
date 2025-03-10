# This will read the values from an excel sheet and plot
# the first column of data against all following columns
# The user chooses whether to plot all point on the same
# plot or separate plots with the 'plot_type' variable'

import pandas as pd
import matplotlib.pyplot as plt

# Customization
file_path = "path/file.xlsx"

# Plots the data
data = pd.read_excel(file_path)
x_val = data.columns[0]

while True:
	plot_type = input('Would you like separate plots (P) or a superimposed plot (I): ')
	if plot_type == "I":
		plt.figure()
		for col in data.columns[1:]:
			plt.plot(data[x_val],data[col], marker='o', label = col)
		plt.title(input("Title: "))
		plt.xlabel(x_val)
		plt.ylabel(input("Y Label: "))
		plt.legend()  # Automatically adds a legend for each line
		plt.grid(True)
		plt.show()
		break
	
	elif plot_type == "P":
		for col in data.columns[1:]:
			plt.figure(col)
			plt.plot(data[x_val],data[col], marker='o')
			plt.title(input(f"Title for {col}: "))
			plt.xlabel(x_val)
			plt.ylabel(input(f"Y Label for {col}: "))
			plt.grid(True)
		plt.show()
		break
	else:
		print('Not a valid plot type. Use "I" or "P"')
