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
    showfliers=False,
    width=0.5,  # Adjusted width to make boxes a quarter of the size
    boxprops={'facecolor': '#26828EFF', 'edgecolor': '#000000'}
)
ax.yaxis.tick_right()  # Moves the ticks to the right
ax.yaxis.set_label_position("right")  # Moves the y-axis label to the right

# Update x-axis labels to include temperature and count
new_labels = [f"{temp}°C, n={counts.get(temp, 0)}" for temp in temperature_order]
ax.set_xticklabels(new_labels)

# Adjust the spacing between boxes by reducing category width
plt.xticks(ticks=range(len(temperature_order)), labels=new_labels, ha='center', fontsize=10)
ax.set_xlim(-0.5, len(temperature_order) - 0.5)

# Customize the plot
plt.title('Effect of Temperature on NMR Yield')
plt.xlabel('Temperature (°C)')
plt.ylabel('Yield')
plt.tight_layout()
plt.show()
