import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield', 'solvent', and 'Time' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['solvent'] = filtered_data['solvent'].astype('category')
filtered_data['Time'] = filtered_data['Time'].astype(int)

# Define the custom order of solvents and times
solvent_order = ["MeCN", "EtOAc", "MeCN/H2O, 2+1", "MeCN/H2O, 1+1", "MeCN/H2O, 1+2"]
time_order = [2, 4, 6, 8]

# Count the number of datapoints for each solvent and time value
solvent_counts = filtered_data['solvent'].value_counts()
time_counts = filtered_data['Time'].value_counts()

# Create a figure with two subplots (side by side)
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Boxplot for solvent vs yield
ax1 = axes[0]
sns.boxplot(
    x='solvent',
    y='yield',
    data=filtered_data,
    order=solvent_order,
    showfliers=False,
    ax=ax1
)

# Update x-axis labels for the first plot
solvent_labels = [f"{solvent}, n={solvent_counts.get(solvent, 0)}" for solvent in solvent_order]
ax1.set_xticklabels(solvent_labels)
ax1.set_xlim(-0.5, len(solvent_order) - 0.5)
ax1.set_title('Effect of Solvent on NMR Yield')
ax1.set_xlabel('Solvent')
ax1.tick_params(axis='x', rotation=45)

# Plot 2: Boxplot for time vs yield
ax2 = axes[1]
sns.boxplot(
    x='Time',
    y='yield',
    data=filtered_data,
    order=time_order,
    showfliers=False,
    ax=ax2
)

# Update x-axis labels for the second plot
time_labels = [f"{time} hr, n={time_counts.get(time, 0)}" for time in time_order]
ax2.set_xticklabels(time_labels)
ax2.set_xlim(-0.5, len(time_order) - 0.5)
ax2.set_title('Effect of Time on NMR Yield')
ax2.set_xlabel('Time (hr)')
ax2.set_ylabel('')  # Remove the y-axis label for the second plot
ax2.tick_params(axis='x', rotation=45)

# Increase space between the subplots
plt.subplots_adjust(wspace=0.3)

# Adjust layout
plt.tight_layout()
plt.show()
