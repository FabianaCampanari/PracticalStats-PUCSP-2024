
**\[[🇧🇷 Português](README.pt_BR.md)\] \[**[🇺🇸 English](README.md)**\]**



<br><br>

![2129d7ad-6afd-4166-9bf1-a4f9c3b9e5cc](https://github.com/user-attachments/assets/faf3e0a3-3610-4c0b-99bb-afb7a765f28d)

<br><br>

## <p align="center">  Practical Statistics and Probability in Python and Excel
#### <p align="center"> [University of Data Science and Artificial Intelligence]() - PUC-SP - 2nd Semester/2024

<br>

#### <p align="center"> [![Sponsor FabianaCampanari ](https://img.shields.io/badge/Sponsor-FabianaCampanari-brightgreen?logo=GitHub)](https://github.com/sponsors/FabianaCampanari) 

<br>


## **Statistics and Probability**
 
This repository, created by [Fabiana 🚀 Campanari](https://linktr.ee/fabianacampanari) in the 2nd semester of 2024, consolidates the materials and code developed for the Statistics and Probability course within the Data Science and Artificial Intelligence program at PUC-SP, under the guidance of [Professor Eric Bacconi Gonçalves](https://www.linkedin.com/in/eric-bacconi-423137/). It is designed to support hands-on learning through exercises, scripts, and datasets.

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

 <p align="center">
<img src="https://github.com/user-attachments/assets/2a7b0742-b1b1-4f4e-ba4b-50dedf6f30bb" />

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

<br>

### 2. Sample Selection

```python

Copy code

# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Define the file path
file_path = 'add_your_dataset_path_here'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Sample Selection

# Simple random sample without replacement with 20 elements
sample = df.sample(20, replace=False)
print(sample)

# Simple random sample without replacement with 20 elements (fixing the random seed)
sample = df.sample(n=20, replace=False, random_state=2903)
print(sample)

# Check the classes of the variable and their proportions
perc_est_civ = df["estado_civil"].value_counts(normalize=True)
print(perc_est_civ)

# Execute equal stratified sample by marital status
sample_strat_equal = df.groupby(['estado_civil'], group_keys=False).apply(lambda x: x.sample(n=10, replace=False, random_state=2903))
print(sample_strat_equal)

# Define desired total
N = 20

# Execute proportional stratified sample by marital status
sample_strat_prop = df.groupby(['estado_civil'], group_keys=False).apply(
    lambda x: x.sample(int(np.rint(N * len(x) / len(df))), random_state=2903)  # Proportional sample calculation
).sample(frac=1, random_state=2903).reset_index(drop=True)  # Shuffle the sample
print(sample_strat_prop)

# Check the proportion of each marital status
perc_est_civ = sample_strat_prop["estado_civil"].value_counts(normalize=True)
print(perc_est_civ)

# Execute equal stratified sample by region of origin
sample_strat_equal = df.groupby(['reg_proc'], group_keys=False).apply(lambda x: x.sample(n=10, replace=False, random_state=2903))
print(sample_strat_equal)

# Execute equal stratified sample by education level
sample_strat_equal = df.groupby(['grau_instrucao'], group_keys=False).apply(lambda x: x.sample(n=10, replace=False, random_state=2903))
print(sample_strat_equal)

# Execute equal stratified sample by region of origin and education level
sample_strat_equal = df.groupby(['reg_proc', 'grau_instrucao'], group_keys=False).apply(lambda x: x.sample(n=10, replace=False, random_state=2903))
print(sample_strat_equal)

# Create an equal stratified sample by education level and region of origin
sample_strat_equal = df.groupby(['grau_instrucao', 'reg_proc'], group_keys=False).apply(lambda x: x.sample(n=min(len(x), 10), replace=False, random_state=2903)).reset_index(drop=True)
print(sample_strat_equal)

# Save the stratified sample to a new Excel file
output_path = 'path_to_save_sample/stratified_sample.xlsx'
sample_strat_equal.to_excel(output_path, index=False)

print(f"The stratified sample has been saved to {output_path}")
```   

<br>

### 3. One-Sample t-Test

```python
Copy code

# Exercise 3 – Test the hypothesis that the salary is equal to 12. What is your conclusion?
# Import pandas library
import pandas as pd

# Import scipy library
import scipy.stats as stats

# File path
file_path = 'add_your_dataset_path_here'

# Load the file into Python
df = pd.read_excel(file_path)
print(df.head())

# Bring only the age variable to perform the test
base_age = df['idade']

# Execute the t-test testing H0: age = 32 and H1: age ≠ 32
result_t_test = stats.ttest_1samp(base_age, 32)
p_value = result_t_test.pvalue
alpha = 0.05

if p_value < alpha:
    print("We reject the null hypothesis (H0).")
else:
    print("We do not reject the null hypothesis (H0).")

# Remember the mean
print(f"Mean age: {df.idade.mean()}")

# Execute the t-test testing H0: age = 34 and H1: age ≠ 34
result_t_test = stats.ttest_1samp(base_age, 34)
p_value = result_t_test.pvalue
alpha = 0.05

# Decision based on p-value
if p_value < alpha:
    print("We reject the null hypothesis (H0).")
else:
    print("We do not reject the null hypothesis (H0).")

# With a p-value of 0.045, which is less than the significance level of 0.05, we reject the null hypothesis. This indicates that there is statistically significant evidence to suggest that the average age of employees is different from 34.

# Execute the t-test testing H0: age = 35 and H1: age ≠ 35
result_t_test = stats.ttest_1samp(base_age, 35)
p_value = result_t_test.pvalue
alpha = 0.05

# Decision based on p-value
if p_value < alpha:
    print("We reject the null hypothesis (H0).")
else:
    print("We do not reject the null hypothesis (H0).")

# With a p-value of 0.2234, which is greater than the significance level of 0.05, we do not reject the null hypothesis. This means that there is not enough evidence to conclude that the average age of employees is different from the hypothesized value (32, 35, or any other value being tested).

# Answering question 3

# Test the hypothesis that the salary is equal to 12. What is your conclusion?
import pandas as pd
import scipy.stats as stats

# File path
file_path = 'add_your_dataset_path_here'

# Load the data
df = pd.read_excel(file_path)
print(df.head())

# Select the variable of interest (salary)
salaries = df['salario']

# Execute the t-test testing H0: salary = 12 and H1: salary ≠ 12
result_t_test = stats.ttest_1samp(salaries, 12)
print(result_t_test)

# Get the p-value from the test result
p_value = result_t_test.pvalue

# Define the significance level
alpha = 0.05

# Interpret the result
p_value = 8.755117588192511e-06

if p_value < alpha:
    print("We reject the null hypothesis (H0).")
else:
    print("We do not reject the null hypothesis (H0).")

# Define the conclusion based on the p-value and the significance level
if p_value < alpha:
    conclusion = "We reject the null hypothesis (H0)."
else:
    conclusion = "We do not reject the null hypothesis (H0)."

# Display the test result and conclusion
print(f"t-test statistic: {result_t_test.statistic}")
print(f"p-value: {result_t_test.pvalue}")
print(conclusion)

# Analysis and Conclusion with p-value and significance level

# In the hypothesis test performed, we tested the null hypothesis (H0) that the average salary of employees is equal to 12 against the alternative hypothesis (H1) that the average salary of employees is different from 12.

# The results of the t-test were as follows:
# - t-test statistic: -4.500727991746298
# - p-value: 8.755117588192511e-06

# With a p-value of approximately 8.76e-06, which is significantly less than the significance level of 0.05, we reject the null hypothesis (H0). This indicates that there is statistically significant evidence to suggest that the average salary of employees is different from 12.

# Therefore, the conclusion of the test is that we reject the null hypothesis (H0) and accept the alternative hypothesis (H1), indicating that the average salary of employees is not equal to 12.
```
<br>

### 4. Two-Sample t-Test

```python

copy code

### Question 4

#### To test the hypothesis that income is equal for the two marital statuses (single and married), we can use the t-test for independent samples. We will follow these steps:
### Visualization

#### 1. Extract income data for singles and married individuals.
#### 2. Perform the t-test for independent samples.
#### 3. Interpret the p-value to accept or reject the null hypothesis.

### Steps in pseudocode:

1. **Import necessary libraries** (pandas and scipy.stats).
2. **Load data from the Excel file**.
3. **Extract income columns for singles and married individuals**.
4. **Perform the t-test for independent samples**.
5. **Interpret the result based on the p-value**.

# Install scipy if necessary
# %pip install scipy pandas
import pandas as pd
from scipy import stats

# Load the data from the Excel file
file_path = 'add_your_dataset_path_here'
df = pd.read_excel(file_path)

# Visualize the first rows of the DataFrame
print(df.head())

# Check the mean salary by marital status group
print(df.groupby(['estado_civil'])['salario'].describe())

# Extract income columns for singles and married individuals
single_income = df[df['estado_civil'] == 's']['salario']
married_income = df[df['estado_civil'] == 'c']['salario']

# Perform the t-test for independent samples
t_stat, p_value = stats.ttest_ind(married_income, single_income, equal_var=False)

# Display the results of the t-test
print("Results of the t-Test:")
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")

# Interpret the result
alpha = 0.05
if p_value < alpha:
    print("Conclusion: We reject the null hypothesis. The incomes are different for the two marital statuses.")
else:
    print("Conclusion: We do not reject the null hypothesis. The incomes are equal for the two marital statuses.")

### Conclusion Results of the t-Test:

#### Interpretation:
 - t-statistic: 4.567472731259726 <br>
 - p-value: 6.527014259249644e-06

The p-value is extremely small (6.527014259249644e-06), much smaller than the common significance level (0.05). This indicates that there is a significant difference in income between the two marital statuses.

**Conclusion:**

We reject the null hypothesis. The incomes are different for the two marital statuses (single and married).
```

<br>

### 5. One-Way ANOVA


```python

copy code

# Import necessary libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# File path
file_path = 'add_your_dataset_path_here'

# Load the data into Python
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Check the average salary by education level
print("Average salary by education level:")
print(df.groupby(['grau_instrucao'])['salario'].describe())

# Create a model to compare salary by education level
model = ols('salario ~ grau_instrucao', data=df).fit()

# Perform ANOVA
anova_result = sm.stats.anova_lm(model)
print("ANOVA Results:")
print(anova_result)

# Interpret the results
alpha = 0.05
p_value = anova_result['PR(>F)'][0]
if p_value < alpha:
    conclusion_anova = "There is a significant difference in salaries among different education levels."
else:
    conclusion_anova = "There is no significant difference in salaries among different education levels."
print(f"Conclusion from ANOVA: {conclusion_anova}")

# Post Hoc Tukey Test to evaluate specific differences
tukey = pairwise_tukeyhsd(endog=df.salario, groups=df.grau_instrucao)
print("Post Hoc Tukey Test Results:")
print(tukey.summary())

# Interpret Tukey results
print("Interpreting Tukey's test results:")
for result in tukey.summary().data[1:]:  # Skip header
    group1, group2, meandiff, p_adj, lower, upper, reject = result
    if reject:
        print(f"Significant difference between {group1} and {group2}: mean difference = {meandiff:.4f}, p-adj = {p_adj:.4f}")
    else:
        print(f"No significant difference between {group1} and {group2}: mean difference = {meandiff:.4f}, p-adj = {p_adj:.4f}")

# Overall conclusion
print("Overall Conclusion:")
print("The results indicate that salary is significantly affected by education level, with higher education corresponding to higher salaries.")
```

<br>

### 6.  Two-Way ANOVA

```python

copy code

# Import necessary libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# File path
file_path = 'add_your_dataset_path_here'

# Load the data into Python
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print("Initial DataFrame:")
print(df.head())

# Check the average salary by education level and marital status
print("\nAverage salary by education level and marital status:")
print(df.groupby(['grau_instrucao', 'estado_civil'])['salario'].describe())

# Generate the model to compare salary by education level and marital status
model = ols('salario ~ grau_instrucao + estado_civil', data=df).fit()

# Apply ANOVA
anova_result = sm.stats.anova_lm(model)
print("\nANOVA Results:")
print(anova_result)

# Interpret the results
alpha = 0.05
p_value_instrucao = anova_result['PR(>F)']['grau_instrucao']
p_value_civil = anova_result['PR(>F)']['estado_civil']

if p_value_instrucao < alpha:
    conclusion_instrucao = "There is a significant difference in salaries among different education levels."
else:
    conclusion_instrucao = "There is no significant difference in salaries among different education levels."

if p_value_civil < alpha:
    conclusion_civil = "There is a significant difference in salaries among different marital statuses."
else:
    conclusion_civil = "There is no significant difference in salaries among different marital statuses."

print(f"\nConclusion from ANOVA for Education Level: {conclusion_instrucao}")
print(f"Conclusion from ANOVA for Marital Status: {conclusion_civil}")

# Post Hoc Tukey Test to evaluate specific differences for marital status
print("\nPost Hoc Tukey Test Results for Marital Status:")
tukey_estado_civil = pairwise_tukeyhsd(endog=df.salario, groups=df.estado_civil)
print(tukey_estado_civil.summary())

# Post Hoc Tukey Test to evaluate specific differences for education level
print("\nPost Hoc Tukey Test Results for Education Level:")
tukey_instrucao = pairwise_tukeyhsd(endog=df.salario, groups=df.grau_instrucao)
print(tukey_instrucao.summary())

# Overall conclusion
print("\nOverall Conclusion:")
print("The results indicate that salary is significantly affected by both education level and marital status.")
```

<br>

### 7. Two-way ANOVA with Interaction

```python

# Import necessary libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# File path
file_path = 'add_your_dataset_path_here'

# Load the data into Python
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print("Initial DataFrame:")
print(df.head())

# Check the average salary by education level and marital status
print("\nAverage salary by education level and marital status:")
print(df.groupby(['grau_instrucao', 'estado_civil'])['salario'].describe())

# Generate the model to compare salary by education level and marital status, including interaction
model = ols('salario ~ grau_instrucao * estado_civil', data=df).fit()

# Apply ANOVA
anova = sm.stats.anova_lm(model)
print("\nANOVA Results:")
print(anova)

# Interpret the results
alpha = 0.05
p_value_instrucao = anova['PR(>F)']['grau_instrucao']
p_value_civil = anova['PR(>F)']['estado_civil']
p_value_interaction = anova['PR(>F)']['grau_instrucao:estado_civil']

# Conclusions from ANOVA
conclusions = {
    "Grau de Instrução": "significant" if p_value_instrucao < alpha else "not significant",
    "Estado Civil": "significant" if p_value_civil < alpha else "not significant",
    "Interação": "significant" if p_value_interaction < alpha else "not significant"
}

for factor, result in conclusions.items():
    print(f"Conclusion from ANOVA for {factor}: There is a {result} effect.")

# Post Hoc Tukey Test for marital status
print("\nPost Hoc Tukey Test Results for Marital Status:")
tukey_estado_civil = pairwise_tukeyhsd(endog=df.salario, groups=df.estado_civil)
print(tukey_estado_civil.summary())

# Post Hoc Tukey Test for education level
print("\nPost Hoc Tukey Test Results for Education Level:")
tukey_instrucao = pairwise_tukeyhsd(endog=df.salario, groups=df.grau_instrucao)
print(tukey_instrucao.summary())

# Overall conclusion
print("\nOverall Conclusion:")
print("The results indicate that salary is significantly affected by both education level and marital status,")
print("and there is also a significant interaction between these two factors.")
```

<br>

### 8. Chi-Square Test for One Variable.

```python

copy code

# Import necessary libraries
import pandas as pd
import scipy.stats as stats

# File path
file_path = 'add_your_dataset_path_here'

# Load the data into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print("Initial DataFrame:")
print(df.head())

# Frequency table for the variable 'reg_proc'
freq_reg_proc = df['reg_proc'].value_counts()
print("\nFrequency of the 'reg_proc' variable:")
print(freq_reg_proc)

# Perform Chi-Square Test
chi2_stat, p_val = stats.chisquare(freq_reg_proc)
print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")

# Interpretation and Conclusion
alpha = 0.05  # Significance level
if p_val < alpha:
    print("Reject the null hypothesis. The distribution of the region of origin is not the same in the sample.")
else:
    print("Fail to reject the null hypothesis. The distribution of the region of origin is the same in the sample.")
```

<br>

9. Chi-Square Test for Independence of Two Variables

```python

copy code

# Import necessary libraries
import pandas as pd
import scipy.stats as stats

# File path
file_path = 'add_your_dataset_path_here'

# Load the data into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print("Initial DataFrame:")
print(df.head())

# Create a contingency table for 'grau_instrucao' and 'reg_proc'
contingency_table = pd.crosstab(df['grau_instrucao'], df['reg_proc'])
print("\nContingency Table:")
print(contingency_table)

# Perform Chi-Square Test of Independence
chi2_stat, p_val, dof, expected = stats.chi2_contingency(contingency_table)
print("\nResults of the Chi-Square Test of Independence:")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

# Interpretation and Conclusion
alpha = 0.05  # Significance level
if p_val < alpha:
    print("\nConclusion: Reject the null hypothesis. The distribution of education levels varies according to the region of origin.")
else:
    print("\nConclusion: Fail to reject the null hypothesis. The distribution of education levels does not vary according to the region of origin.")
```




<br><br>

<p align="center"> <a href="#top">Back to Top</a>


#
###### <p align="center"> Copyright 2024 Fabiana Campanari. Code released under the [MIT license.](https://github.com/FabianaCampanari/FabianaCampanari/blob/66325d147794b5fc4688d56e6b78e8cdf42946e4/LICENSE)


