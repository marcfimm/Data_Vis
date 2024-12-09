import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Borylation_Thermal_round_6.csv')  # Replace with the path to your file

# Filter rows where 'priority' is -1
filtered_data = data[data['priority'] == -1].copy()  # Make a copy to avoid SettingWithCopyWarning

# Convert columns to appropriate data types using .loc[] to avoid the warning
filtered_data.loc[:, 'Time'] = filtered_data['Time'].astype(float)
filtered_data.loc[:, 'concentration'] = filtered_data['concentration'].astype(float)
filtered_data.loc[:, 'yield'] = filtered_data['yield'].astype(float)

# Identify numerical and categorical columns
numerical_columns = filtered_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_columns = filtered_data.select_dtypes(include=['object', 'category']).columns.tolist()

# Ensure 'yield' is in the dataset
if 'yield' not in filtered_data.columns:
    raise ValueError("The column 'yield' is not present in the dataset.")

# Visualize the effect of categorical variables on yield using dot plots
for cat_col in categorical_columns:
    if cat_col != 'priority':  # Ignore 'priority' column
        plt.figure(figsize=(8, 6))
        sns.stripplot(x=cat_col, y='yield', data=filtered_data, jitter=True, color='blue', alpha=0.6)
        plt.title(f'Effect of {cat_col} on Yield')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
