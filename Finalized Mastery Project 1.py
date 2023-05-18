#!/usr/bin/env python
# coding: utf-8

# In[235]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import scipy.stats as st
from statsmodels.stats import weightstats as stests


# In[236]:


data = pd.read_csv('query_results2.csv')


# In[237]:


data.head()


# In[238]:


# Set the plot style
sns.set(style="white")

# Set the color palette
palette = sns.color_palette()

# Grouping data by group and calculating total spent and average spent
group_spent = data.groupby('group')['total_spent'].agg(['sum', 'mean'])

# Plotting the total spent per group
plt.figure(figsize=(8, 6))
plt.bar(group_spent.index, group_spent['sum'], color=palette[1::-1])
plt.xlabel('Group')
plt.ylabel('Total Spent')
plt.title('Total Spent per Group')

# Placing total values on top of the bars
for i, value in enumerate(group_spent['sum']):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom')

plt.show()

# Plotting the average spent per group
plt.figure(figsize=(8, 6))
plt.bar(group_spent.index, group_spent['mean'], color=palette[1::-1])
plt.xlabel('Group')
plt.ylabel('Average Spent')
plt.title('Average Spent per Group')

# Placing average values on top of the bars
for i, value in enumerate(group_spent['mean']):
    plt.text(i, value, '${:.2f}'.format(value), ha='center', va='bottom')

plt.show()

# Group the data by 'group' and calculate the sum of 'converted' for each group
grouped = data.groupby('group')['converted'].sum()

# Plot the bar graph
plt.figure(figsize=(8, 6))
plt.bar(grouped.index, grouped.values)
plt.xlabel('Group')
plt.ylabel('Number of Conversions')
plt.title('Conversions by Group')

# Add numbers on top of the bars
for i, v in enumerate(grouped.values):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.show()

# Group the data by 'group' and calculate the sum of 'converted' and total count for each group
grouped = data.groupby('group')['converted'].agg(['sum', 'count'])

# Calculate the conversion rate
grouped['conversion_rate'] = grouped['sum'] / grouped['count']

# Plot the conversion rate per group
plt.figure(figsize=(8, 6))
plt.bar(grouped.index, grouped['conversion_rate'], color=palette[1::-1])
plt.xlabel('Group')
plt.ylabel('Conversion Rate')
plt.title('Conversion Rate per Group')

# Add conversion rate values on top of the bars
for i, value in enumerate(grouped['conversion_rate']):
    plt.text(i, value, f'{value:.2%}', ha='center', va='bottom')

plt.show()


# ### T-test comparing means

# In[239]:


control_group = data[data['group'] == 'A']['total_spent']
test_group = data[data['group'] == 'B']['total_spent']

tTest, pValue = stats.ttest_ind(control_group, test_group, equal_var = False)


# In[240]:


tTest


# In[241]:


pValue


# ### Confidence Interval for comparing means

# In[242]:


# mean and standard error for control group
control_mean = np.mean(control_group)
control_sem = st.sem(control_group)

# 95% confidence interval for control group
control_ci = st.t.interval(0.95, len(control_group)-1, loc=control_mean, scale=control_sem)

# mean and standard error for test group
test_mean = np.mean(test_group)
test_sem = st.sem(test_group)

# 95% confidence interval for test group
test_ci = st.t.interval(0.95, len(test_group)-1, loc=test_mean, scale=test_sem)


# In[243]:


control_ci


# In[244]:


test_ci


# ### Confidence interval for the difference in the average amount spent per user between the treatment and the control.
# 

# In[245]:


# Calculate the mean and standard deviation for each group
control_mean = np.mean(control_group)
test_mean = np.mean(test_group)
control_std = np.std(control_group, ddof=1)
test_std = np.std(test_group, ddof=1)

# Calculate the standard error of the difference in means
n_control = len(control_group)
n_test = len(test_group)
se_difference = np.sqrt((control_std**2 / n_control) + (test_std**2 / n_test))

# Calculate the degrees of freedom
df = n_control + n_test - 2

# Calculate the critical value from the t-distribution
alpha = 0.05  # Confidence level (e.g., 95% confidence)
critical_value = stats.t.ppf(1 - alpha / 2, df)

# Calculate the margin of error
margin_of_error = critical_value * se_difference

# Calculate the confidence interval
ci_low = (test_mean - control_mean) - margin_of_error
ci_high = (test_mean - control_mean) + margin_of_error


# In[246]:


ci_low, ci_high


# # P = 0.944 is statistically insignificant. We fail to reject the null hypothesis that there is no difference in the mean amount spent per user between the control and treatment.

# ### Z-test comparing proportions

# In[247]:


control_group = data[data['group'] == 'A']['converted']
test_group = data[data['group'] == 'B']['converted']

zTest, pValue = stests.ztest(control_group, test_group, alternative='two-sided')


# In[248]:


zTest


# In[249]:


pValue


# ### Confidence Interval for proportions

# In[250]:


dx = data[["group", "converted"]].dropna()


# In[251]:


pd.crosstab(dx.converted, dx.group)


# In[252]:


from statsmodels.stats.proportion import proportion_confint

# control
count_a = 955  # Number of successes
n_a = 23388 + 955  # Total number of observations
alpha = 0.05  # Confidence level (e.g., 95% confidence)
ci_low, ci_high = proportion_confint(count_a, n_b, alpha, method='normal')


# In[253]:


ci_low, ci_high


# In[254]:


# test
count_b = 1139  # Number of successes
n_b = 23461 + 1139  # Total number of observations
alpha = 0.05  # Confidence level (e.g., 95% confidence)
ci_low, ci_high = proportion_confint(count_b, n_b, alpha, method='normal')


# In[255]:


ci_low, ci_high


# In[256]:


control_ci = (0.036407252103522136, 0.041235024319242086)
test_ci = (0.043674898684431224, 0.04892672733182894)

# Calculate the difference in proportions
diff = (test_ci[0] - control_ci[1], test_ci[1] - control_ci[0])


# In[257]:


diff


# # P = 0.0001 is statistically significant. We reject the null hypothesis that there is no difference in the user conversion rate between the control and treatment.
