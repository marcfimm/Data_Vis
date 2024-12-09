import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield' and 'oxidant' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['oxidant'] = filtered_data['oxidant'].astype('category')

# Define the custom order of oxidants
oxidant_order = ["K2S2O8", "(Bu4N)2S2O8", "(NH4)2S2O8"]

# Count the number of datapoints for each oxidant
counts = filtered_data['oxidant'].value_counts()

# Create the boxplot
plt.figure(figsize=(10, 6))
ax = sns.boxplot(
    x='oxidant',
    y='yield',
    data=filtered_data,
    order=oxidant_order,
    showfliers=False
)

# Update x-axis labels to include oxidant and count
new_labels = [f"{oxidant}, n={counts.get(oxidant, 0)}" for oxidant in oxidant_order]
ax.set_xticklabels(new_labels)

# Customize the plot
plt.title('Effect of Oxidant on NMR Yield')
plt.xlabel('Oxidant')
plt.ylabel('Yield')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
