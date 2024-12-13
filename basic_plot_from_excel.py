# This will read the values from an excel sheet and plot
# the first column of data against all following columns

import pandas as pd
import matplotlib.pyplot as plt

# Load excel file
file_path = "C:/Users/Bryan Keating/OneDrive - Rutgers University/Senior Year/Senior Fall/Multiphysics Simulations/Homework Assignments/Final Project/Simulation Results Backup.xlsx"
data = pd.read_excel(file_path)

print(data.columns)