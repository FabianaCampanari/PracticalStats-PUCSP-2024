
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

# Importing pandas library for data manipulation and analysis
import pandas as pd

# Define the file path to the dataset
Caminho = '/path/to/your/file/cadastro_funcionarios.xlsx'

# Load the dataset into a DataFrame
df = pd.read_excel(Caminho)

# Display the first 5 rows of the dataset
df.head()

# --- Descriptive Statistics for 'idade' (age) ---

# Generate descriptive statistics for the 'idade' (age) column
print("Descriptive statistics for 'idade':")
print(df.idade.describe())

# Calculate the range (amplitude) of the 'idade' column
ampl_idade = df.idade.max() - df.idade.min()
print("\nAmplitude of 'idade':", ampl_idade)

# Calculate the mode of the 'idade' column
moda_idade = df.idade.mode()
print("\nMode of 'idade':", moda_idade)

# Calculate the variance of the 'idade' column
var_idade = df.idade.var()
print("\nVariance of 'idade':", var_idade)

# Calculate additional statistics for 'idade'
min_idade = df.idade.min()
max_idade = df.idade.max()
media_idade = df.idade.mean()
mediana_idade = df.idade.median()
desvpad_idade = df.idade.std()

print(f"\nMin: {min_idade}, Max: {max_idade}, Mean: {media_idade}, Median: {mediana_idade}, Std Dev: {desvpad_idade}")

# Calculate the coefficient of variation (CV) for 'idade'
cv_idade = df.idade.std() / df.idade.mean()
print("\nCoefficient of variation (CV) of 'idade':", cv_idade)

# --- Grouped Descriptive Statistics for 'idade' by 'reg_proc' (region) ---

# Generate descriptive statistics for 'idade' grouped by 'reg_proc' (region)
print("\nDescriptive statistics for 'idade' grouped by 'reg_proc':")
print(df.groupby('reg_proc')['idade'].describe())

# Calculate the range (amplitude) for 'idade' by region
ampl_idade_reg = df.groupby('reg_proc')['idade'].max() - df.groupby('reg_proc')['idade'].min()
print("\nAmplitude of 'idade' by region:")
print(ampl_idade_reg)

# Calculate the variance of 'idade' by region
var_idade_reg = df.groupby('reg_proc')['idade'].var()
print("\nVariance of 'idade' by region:")
print(var_idade_reg)

# Calculate the coefficient of variation (CV) for 'idade' by region
cv_idade_reg = df.groupby('reg_proc')['idade'].std() / df.groupby('reg_proc')['idade'].mean()
print("\nCoefficient of variation (CV) of 'idade' by region:")
print(cv_idade_reg)

# Calculate the mode of 'idade' by region
moda_idade_reg = df.groupby('reg_proc')['idade'].agg(pd.Series.mode)
print("\nMode of 'idade' by region:")
print(moda_idade_reg)

# --- Descriptive Statistics for 'salario' (salary) ---

# Generate descriptive statistics for 'salario' (salary)
print("\nDescriptive statistics for 'salario':")
print(df.salario.describe())

# Calculate the range (amplitude) of 'salario'
ampl_salario = df['salario'].max() - df['salario'].min()
print("\nAmplitude of 'salario':", ampl_salario)

# Calculate the mode of 'salario'
moda_salario = df.salario.mode()
print("\nMode of 'salario':", moda_salario)

# Calculate the variance of 'salario'
var_salario = df.salario.var()
print("\nVariance of 'salario':", var_salario)

# Calculate the coefficient of variation (CV) for 'salario'
cv_salario = df['salario'].std() / df['salario'].mean()
print("\nCoefficient of variation (CV) of 'salario':", cv_salario)

# --- Grouped Descriptive Statistics for 'salario' by 'grau_instrucao' (education level) ---

# Generate descriptive statistics for 'salario' grouped by 'grau_instrucao' (education level)
print("\nDescriptive statistics for 'salario' grouped by 'grau_instrucao':")
print(df.groupby('grau_instrucao')['salario'].describe())

# Calculate the range (amplitude) of 'salario' by 'grau_instrucao'
ampl_salario_grau = df.groupby('grau_instrucao')['salario'].max() - df.groupby('grau_instrucao')['salario'].min()
print("\nAmplitude of 'salario' by 'grau_instrucao':")
print(ampl_salario_grau)

# Calculate the mode of 'salario' by 'grau_instrucao'
moda_salario_grau = df.groupby('grau_instrucao')['salario'].agg(lambda x: pd.Series.mode(x)[0])
print("\nMode of 'salario' by 'grau_instrucao':")
print(moda_salario_grau)

# Calculate the variance of 'salario' by 'grau_instrucao'
var_salario_grau = df.groupby('grau_instrucao')['salario'].var()
print("\nVariance of 'salario' by 'grau_instrucao':")
print(var_salario_grau)

# Calculate the coefficient of variation (CV) for 'salario' by 'grau_instrucao'
cv_salario_grau = df.groupby('grau_instrucao')['salario'].std() / df.groupby('grau_instrucao')['salario'].mean()
print("\nCoefficient of variation (CV) of 'salario' by 'grau_instrucao':")
print(cv_salario_grau)
```


```python

Copy code

# Importing the necessary library
import pandas as pd

# Define the file path to the dataset
file_path = '/Users/fabicampanari/Desktop/_8-Prova Matematematica/1-statiscalMeasures_ Hypothesis Testing II./1🇧🇷-statiscalMeasures_ Hypothesis Testing II./answeredCodes_statiscalMeasures/cadastro_funcionarios.xlsx'

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


