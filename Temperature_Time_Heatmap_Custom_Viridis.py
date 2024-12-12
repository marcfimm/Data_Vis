import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield', 'T' (Temperature), and 'Time' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['T'] = filtered_data['T'].astype(int)
filtered_data['Time'] = filtered_data['Time'].astype(int)

# Pivot the data to create a matrix of average yields
pivot_data_yield = filtered_data.pivot_table(values='yield', index='Time', columns='T', aggfunc='mean')

# Pivot the data to create a matrix of counts (number of experiments)
pivot_data_counts = filtered_data.pivot_table(values='yield', index='Time', columns='T', aggfunc='count')

# Generate custom annotations with `n=` above the counts
annotations = pivot_data_counts.applymap(lambda x: f"n={x}" if pd.notnull(x) else "")

# Define the custom colormap (cut off the top 25% of 'viridis')
original_cmap = plt.cm.viridis
n_colors = original_cmap.N
cutoff = int(n_colors * 0.75)  # 75% of the colormap
colors = original_cmap(np.linspace(0, 0.75, cutoff))  # Extract first 75%
custom_cmap = ListedColormap(colors)

# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(
    pivot_data_yield,
    annot=annotations,
    fmt='',  # Prevent formatting issues with the annotations
    cmap=custom_cmap,  # Use the custom colormap
    cbar_kws={'label': 'Average Yield'},
    annot_kws={'size': 10},  # Annotation text size
    linewidths=0.5,  # Adds a small line between the boxes
    linecolor='gray'  # Line color between boxes
)

# Customize the plot
plt.title('Average Yield and Number of Experiments (Temperature, Time correlation)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Time (hr)')
plt.tight_layout()
plt.show()
