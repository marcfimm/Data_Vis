import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield' and 'T' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['T'] = filtered_data['T'].astype(int)

# Define the custom order of temperatures
temperature_order = [50, 70, 90]

# Count the number of datapoints for each temperature
counts = filtered_data['T'].value_counts()

# Create the boxplot
plt.figure(figsize=(10, 6))
ax = sns.boxplot(
    x='T',
    y='yield',
    data=filtered_data,
    order=temperature_order,
    showfliers=False
)

# Update x-axis labels to include temperature and count
new_labels = [f"{temp}°C, n={counts.get(temp, 0)}" for temp in temperature_order]
ax.set_xticklabels(new_labels)

# Customize the plot
plt.title('Effect of Temperature on NMR Yield')
plt.xlabel('Temperature (°C)')
plt.ylabel('Yield')
plt.tight_layout()
plt.show()
