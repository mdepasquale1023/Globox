# Analysis on the Impact of Banner Implementation on User Engagement and Spending

# Introduction
GloBox recently conducted an A/B test to evaluate the effectiveness of a new banner promoting the food and drink category on its website. The goal was to determine whether the banner influenced user spending and conversion rates. This report presents the findings of the test, providing insights into user behavior and offering recommendations for future marketing strategies.

# Methodology
### Data Aggregation
The initial data extraction and aggregation were performed using SQL. This process involved querying multiple tables to retrieve relevant user information, including group assignment, spending behavior, and conversion events.
Specific SQL queries were utilized to join user data with transaction data, ensuring a comprehensive dataset that included user group assignments, spending amounts, and conversion indicators.
Data cleaning steps were applied during the SQL aggregation phase, where null values in the spending column were treated appropriately to maintain data integrity.
Statistical Analysis:
After data aggregation, the dataset was imported into a Python environment for detailed statistical analysis.
A T-test was conducted to compare the average spending between Group A (control) and Group B (test), providing insights into the banner's impact on spending behavior.
A Z-test for two proportions was used to assess the difference in conversion rates between the two groups, determining the effectiveness of the banner in influencing user purchases.
### A/B Test Design
Users were randomly assigned to Group A or Group B to ensure the test's validity.
Group A users did not see the banner, while Group B users were exposed to it, allowing for a direct comparison of user behavior between the two groups.
Results
1. User Distribution
Total users: 48,943
Users in Group A: 24,343
Users in Group B: 24,600

2. Spending Analysis
The T-test did not reveal a statistically significant difference in average spending between Group A and Group B.
Mean spending in Group A: $3.37
Mean spending in Group B: $3.39

3. Conversion Rate Analysis
Overall conversion rate: 4.28%
Conversion rate for Group A: 3.92%
Conversion rate for Group B: 4.63%
The Z-test indicated a statistically significant difference in conversion rates, with Group B showing higher conversions.

# Discussion
The analysis suggests that while the banner did not significantly impact average user spending, it did have a positive effect on the conversion rate. This indicates that the banner may have influenced more users in Group B to make a purchase, even if it didn't affect the amount spent per user.

# Conclusions
The banner's introduction is associated with a higher conversion rate but not with increased spending per user.
These findings suggest that the banner effectively attracts user attention and encourages purchasing behavior, even though it doesn't lead to higher spending.

# Recommendations
Implement the Banner: Consider adopting the banner across the site, given its positive impact on conversion rates.
Perform a segmentation analysis on user segments to identify specific groups that may be more influenced by the banner.
Continue monitoring spending and conversion rates to ensure the banner maintains its effectiveness over time.

**Refer to the report for the appendix to see detailed statistical analysis output, data collection methodology, and graphs and charts illustrating the findings.


