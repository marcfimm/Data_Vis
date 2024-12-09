import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield' and 'Time' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['Time'] = filtered_data['Time'].astype(int)

# Define the custom order of times
time_order = [2, 4, 6, 8]

# Count the number of datapoints for each time value
counts = filtered_data['Time'].value_counts()

# Create the boxplot
plt.figure(figsize=(10, 6))
ax = sns.boxplot(
    x='Time',
    y='yield',
    data=filtered_data,
    order=time_order,
    showfliers=False
)

# Update x-axis labels to include time and count
new_labels = [f"{time} hr, n={counts.get(time, 0)}" for time in time_order]
ax.set_xticklabels(new_labels)

# Customize the plot
plt.title('Effect of Time on NMR Yield')
plt.xlabel('Time (hr)')
plt.ylabel('Yield')
plt.tight_layout()
plt.show()
