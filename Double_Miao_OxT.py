import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield', 'oxidant', and 'T' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['oxidant'] = filtered_data['oxidant'].astype('category')
filtered_data['T'] = filtered_data['T'].astype(int)

# Define the custom order of oxidants and temperatures (swap the two oxidants as requested)
oxidant_order = ["K2S2O8", "(NH4)2S2O8", "(Bu4N)2S2O8"]
temperature_order = [50, 70, 90]

# Count the number of datapoints for each oxidant and temperature
oxidant_counts = filtered_data['oxidant'].value_counts()
temperature_counts = filtered_data['T'].value_counts()

# Create a figure with two subplots (side by side)
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Boxplot for oxidant vs yield
ax1 = axes[0]
sns.boxplot(
    x='oxidant',
    y='yield',
    data=filtered_data,
    order=oxidant_order,
    showfliers=True,
    whis=[0, 100],
    ax=ax1
)

# Update x-axis labels for the first plot
oxidant_labels = [f"{oxidant}, n={oxidant_counts.get(oxidant, 0)}" for oxidant in oxidant_order]
ax1.set_xticklabels(oxidant_labels)
ax1.set_xlim(-0.5, len(oxidant_order) - 0.5)
ax1.set_title('Effect of Oxidant on NMR Yield')
ax1.set_xlabel('Oxidant')
ax1.set_ylabel('Yield')
ax1.tick_params(axis='x', rotation=45)

# Plot 2: Boxplot for temperature vs yield
ax2 = axes[1]
sns.boxplot(
    x='T',
    y='yield',
    data=filtered_data,
    order=temperature_order,
    showfliers=False,
    width=0.5,  # Adjusted width to make boxes a quarter of the size
    ax=ax2
)

# Update x-axis labels for the second plot
temperature_labels = [f"{temp}°C, n={temperature_counts.get(temp, 0)}" for temp in temperature_order]
ax2.set_xticklabels(temperature_labels)
ax2.set_xlim(-0.5, len(temperature_order) - 0.5)
ax2.set_title('Effect of Temperature on NMR Yield')
ax2.set_xlabel('Temperature (°C)')
ax2.set_ylabel('')  # Remove the y-axis label for the second plot
ax2.tick_params(axis='x', rotation=45)

# Increase space between the subplots
plt.subplots_adjust(wspace=0.3)

# Adjust layout
plt.tight_layout()
plt.show()
