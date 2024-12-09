import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6_plot.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()

# Convert 'yield' and 'Solvent' columns to appropriate data types
filtered_data['yield'] = filtered_data['yield'].astype(float)
filtered_data['solvent'] = filtered_data['solvent'].astype('category')

# Define the custom order of solvents
solvent_order = ["MeCN", "EtOAc", "MeCN/H2O, 2+1","MeCN/H2O, 1+1", "MeCN/H2O, 1+2"]

# Visualize the effect of Solvent on Yield using a boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='solvent', y='yield', data=filtered_data, order=solvent_order,showfliers=False)
plt.title('Effect of Solvent on NMR Yield')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()