
<br><br>

![2129d7ad-6afd-4166-9bf1-a4f9c3b9e5cc](https://github.com/user-attachments/assets/faf3e0a3-3610-4c0b-99bb-afb7a765f28d)

<br><br>

## <p align="center">  Practical Stats - PUCSP  2nd Semester 2024 

<br>

#### <p align="center"> [![Sponsor FabianaCampanari ](https://img.shields.io/badge/Sponsor-FabianaCampanari-brightgreen?logo=GitHub)](https://github.com/sponsors/FabianaCampanari)

<br>


## **Statistics and Probability**
 
This repository, created by [Fabiana 🚀 Campanari](https://linktr.ee/fabianacampanari) in the 2nd semester of 2024, consolidates the materials and code developed for the Statistics and Probability course within the Data Science and Artificial Intelligence program at PUC-SP, under the guidance of [Professor Eric Bacconi Gonçalves](https://www.linkedin.com/in/eric-bacconi-423137/)
). It is designed to support hands-on learning through exercises, scripts, and datasets.

## Repository Contents:

<br>

- **Python Scripts**: This section includes scripts for a wide range of statistical analyses, covering key topics such as distributions, population and sample concepts, and hypothesis testing. Calculations include:
  - **Central Tendency**: Mean, median, and mode
  - **Dispersion**: Standard deviation, variance, and range
  - **Positional Measures**: Percentiles and quartiles (Q1, Q2, Q3)
  - **Distribution Shape**: Skewness and kurtosis
  - **Confidence Intervals** for estimating population parameters
  - **Correlation and Covariance** for bivariate analysis
 
 <br>   

- **Practical Exercises**: Available in Python and Excel, these exercises provide hands-on practice in calculating statistical measures and applying concepts, including:
  - **Analysis of Variance (ANOVA)**: Comparing means across multiple groups
  - **Hypothesis Testing**: Null hypothesis (\( H_0 \)) tests, such as T-tests (one-sample, independent, and paired), ANOVA, and Chi-square tests
  - **Regression Analysis**: Linear regression models for predictive analysis
  - **Probability**: Exercises covering probability distributions, expected value, and variance
 
 <br>   

- **Statistical Tests**: This section includes implementations of statistical tests tailored to analyze variables like age and salary, categorized by region and educational level. Each test includes the process of setting up and testing the null hypothesis (\( H_0 \)) for statistical significance.

<br>  

- **Support Materials**: Supplementary documentation on probability, relevant datasets, and homework assignments to reinforce key concepts.

<br>

## Study Topics:

This repository provides a comprehensive foundation in core topics, including Descriptive Statistics, Probability Distributions, Population and Sample, Hypothesis Testing I and II (featuring null hypothesis (\( H_0 \)) testing), and Regression Analysis. It serves as a practical tool for building statistical and analytical skills.


## Statistical Measures Analysis in Python

This repository contains Python scripts for descriptive statistical analysis of employee salary and age data, including analyses for the entire dataset as well as subgrouped by education level and region.

## Features:

Descriptive statistics: Mean, Median, Mode, Variance, Standard Deviation, Coefficient of Variation (CV), and Amplitude (Range).
Grouped analysis: The same statistics calculated by grouping data based on region and education level.
Designed for students: Easy-to-follow code with comments and explanations for each step.

<br>

## Dataset:

The dataset used in this analysis contains employee details, including their age, salary, region of origin (reg_proc), and education level (grau_instrucao).
[Click here to get the Dataset](https://github.com/FabianaCampanari/statisticalMeasures-python-/tree/a9e92b1cbce36fa5f26edeadef937981012f0a98/Dataset)

<br>

## Getting Started:

### To run this script, ensure you have the following:

- Python 3 installed.

- Necessary libraries (pandas) installed.

- An Excel file containing the dataset in the appropriate format.


## Codes

### 1. Statics Measures

```python

Copy code

# Importing the necessary library
import pandas as pd

# Define the file path to the dataset
file_path = 'add_your_dataset_path_here'

# Load the dataset into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the dataset
df.head()

# --- Descriptive Statistics for 'SALARIO' (salary) ---

# Generate descriptive statistics for the 'SALARIO' column
print("Descriptive statistics for 'SALARIO':")
print(df.salario.describe())

# Calculate the range (amplitude) of the 'SALARIO' column
ampl_salario = df['salario'].max() - df['salario'].min()
print("\nAmplitude of 'SALARIO':", ampl_salario)

# Calculate the mode of the 'SALARIO' column
moda_salario = df.salario.mode()[0]
print("\nMode of 'SALARIO':", moda_salario)

# Calculate the variance of the 'SALARIO' column
var_salario = df.salario.var()
print("\nVariance of 'SALARIO':", var_salario)

# Calculate the coefficient of variation (CV) for 'SALARIO'
cv_salario = df.salario.std() / df.salario.mean()
print("\nCoefficient of variation (CV) of 'SALARIO':", cv_salario)

# --- Descriptive Statistics for 'SALARIO' by 'grau_instrucao' (educational level) ---

# Generate descriptive statistics for 'SALARIO' grouped by 'grau_instrucao' (education level)
print("\nDescriptive statistics for 'SALARIO' grouped by 'grau_instrucao':")
print(df.groupby('grau_instrucao')['salario'].describe())

# Calculate the range (amplitude) of 'SALARIO' by 'grau_instrucao'
ampl_salario_grau = df.groupby('grau_instrucao')['salario'].max() - df.groupby('grau_instrucao')['salario'].min()
print("\nAmplitude of 'SALARIO' by 'grau_instrucao':")
print(ampl_salario_grau)

# Calculate the mode of 'SALARIO' by 'grau_instrucao'
moda_salario_grau = df.groupby('grau_instrucao')['salario'].agg(lambda x: pd.Series.mode(x)[0])
print("\nMode of 'SALARIO' by 'grau_instrucao':")
print(moda_salario_grau)

# Calculate the variance of 'SALARIO' by 'grau_instrucao'
var_salario_grau = df.groupby('grau_instrucao')['salario'].var()
print("\nVariance of 'SALARIO' by 'grau_instrucao':")
print(var_salario_grau)

# Calculate the coefficient of variation (CV) for 'SALARIO' by 'grau_instrucao'
cv_salario_grau = df.groupby('grau_instrucao')['salario'].std() / df.groupby('grau_instrucao')['salario'].mean()
print("\nCoefficient of variation (CV) of 'SALARIO' by 'grau_instrucao':")
print(cv_salario_grau)

# Summary of key descriptive statistics
print("\nSummary for 'SALARIO' as a Whole:")
print(f"\nAmplitude: {ampl_salario}")
print(f"\nMode: {moda_salario}")
print(f"\nVariance: {var_salario}")
print(f"\nCoefficient of variation (CV): {cv_salario}")

print("\nSummary by 'grau_instrucao':")
print(f"\nAmplitude by 'grau_instrucao': \n{ampl_salario_grau}")
print(f"\nMode by 'grau_instrucao': \n{moda_salario_grau}")
print(f"\nVariance by 'grau_instrucao': \n{var_salario_grau}")
print(f"\nCoefficient of variation (CV) by 'grau_instrucao': \n{cv_salario_grau}")
```



 

<br><br>

<p align="center"> <a href="#top">Back to Top</a>


















#
###### <p align="center"> Copyright 2024 Fabiana Campanari. Code released under the [MIT license.](https://github.com/FabianaCampanari/FabianaCampanari/blob/66325d147794b5fc4688d56e6b78e8cdf42946e4/LICENSE)


