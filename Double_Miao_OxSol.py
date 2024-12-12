import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield', 'oxidant', 'T', and 'solvent' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['oxidant'] = filtered_data['oxidant'].astype('category')
filtered_data['T'] = filtered_data['T'].astype(int)
filtered_data['solvent'] = filtered_data['solvent'].astype('category')

# Define the custom order of oxidants and solvents
oxidant_order = ["K2S2O8", "(NH4)2S2O8", "(Bu4N)2S2O8"]
solvent_order = ["MeCN", "EtOAc", "MeCN/H2O, 2+1", "MeCN/H2O, 1+1", "MeCN/H2O, 1+2"]

# Count the number of datapoints for each oxidant and solvent
oxidant_counts = filtered_data['oxidant'].value_counts()
solvent_counts = filtered_data['solvent'].value_counts()

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
    ax=ax1,
    patch_artist=True,
    boxprops={'facecolor': '#26828EFF', 'edgecolor': '#000000'}
)

# Update x-axis labels for the first plot
oxidant_labels = [f"{oxidant}, n={oxidant_counts.get(oxidant, 0)}" for oxidant in oxidant_order]
ax1.set_xticklabels(oxidant_labels)
ax1.set_xlim(-0.5, len(oxidant_order) - 0.5)
ax1.set_title('Effect of Oxidant on NMR Yield')
ax1.set_xlabel('Oxidant')
ax1.set_ylabel('Yield')
ax1.tick_params(axis='x', rotation=45)

# Plot 2: Boxplot for solvent vs yield
ax2 = axes[1]
sns.boxplot(
    x='solvent',
    y='yield',
    data=filtered_data,
    order=solvent_order,
    showfliers=False,
    ax=ax2,
    boxprops={'facecolor': '#26828EFF', 'edgecolor': '#000000'}
)

# Update x-axis labels for the second plot
solvent_labels = [f"{solvent}, n={solvent_counts.get(solvent, 0)}" for solvent in solvent_order]
ax2.set_xticklabels(solvent_labels)
ax2.set_xlim(-0.5, len(solvent_order) - 0.5)
ax2.set_title('Effect of Solvent on NMR Yield')
ax2.set_xlabel('Solvent')
ax2.set_ylabel('')  # Remove the y-axis label for the second plot
ax2.tick_params(axis='x', rotation=45)

# Increase space between the subplots
plt.subplots_adjust(wspace=0.3)

# Adjust layout
plt.tight_layout()
plt.show()
