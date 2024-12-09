import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_with_yield(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Ensure the yield column is numeric for correlation
    df['yield'] = pd.to_numeric(df['yield'], errors='coerce')
    
    # Select numeric columns only
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Check if 'yield' is among numeric columns
    if 'yield' not in numeric_columns:
        print("The 'yield' column is not numeric or missing.")
        return
    
    # Filter relevant numeric columns for the correlation
    numeric_columns = [col for col in numeric_columns if col != 'priority']  # Ignore priority
    
    # Pairplot to visualize correlations
    sns.pairplot(df, vars=numeric_columns, diag_kind='kde', corner=True)
    plt.suptitle("Correlations with Yield", y=1.02)
    plt.show()

# Example usage
csv_file_path = "Borylation_Thermal_round_6.csv"  # Replace with your actual file path
plot_correlation_with_yield(csv_file_path)
