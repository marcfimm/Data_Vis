import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield', 'T' (Temperature), and 'Time' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['T'] = filtered_data['T'].astype(int)
filtered_data['Time'] = filtered_data['Time'].astype(int)

# Pivot the data to create a matrix of Yield values indexed by Time and Temperature
pivot_data = filtered_data.pivot_table(values='yield', index='Time', columns='T', aggfunc='mean')

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_data, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Average Yield'}, fmt=".1f")

# Customize the plot
plt.title('Combined Effect of Temperature and Time on NMR Yield')
plt.xlabel('Temperature (°C)')
plt.ylabel('Time (hr)')
plt.tight_layout()
plt.show()
