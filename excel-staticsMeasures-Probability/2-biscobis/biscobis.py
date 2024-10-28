import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_statistics(data):
    # [Previous statistics calculation remains the same]

# Load the dataset
df = pd.read_csv('biscobis-statistical-measures.csv', skiprows=2, encoding='latin1')

# Calculate statistics for each column
statistics = df.apply(calculate_statistics)

# Transpose the results for better readability
statistics_transposed = statistics.transpose()

# Display and save the results
print(statistics_transposed)
statistics_transposed.to_csv('biscobis_detailed_statistics.csv')

# Create visualizations
plt.figure(figsize=(12, 6))
sns.boxplot(data=df)
plt.title('Distribution of Ratings by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot_biscobis.png')
plt.show()  # Added to display the boxplot
plt.close()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Categories')
plt.tight_layout()
plt.savefig('heatmap_correlation_biscobis.png')
plt.show()  # Added to display the heatmap
plt.close()

def create_histogram(data, column, bins=10):
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], bins=bins, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig(f'histogram_{column.lower().replace(" ", "_")}.png')
    plt.show()  # Added to display each histogram
    plt.close()

for column in df.columns:
    create_histogram(df, column)

print("Analysis complete. Results saved in CSV and PNG files.")
