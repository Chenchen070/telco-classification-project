# Telco-churn-classification-project

## Project Goals

My goal is to identify key drivers of churn, which group of customers are more likely to churn. Then make recommendations for changes so that we can reduce the monthly churn rate and increase customer retention.

## Project Description

* How to reduce the customer churn rate is pretty much every single company's all-year-round mission. What kind of marketing strategies the company need to use. What is the main group the company need to focus on base on their products. What kind of services the company can offer to retain the current customers and attract more new customers. 
* In this report, we will analyze the attributes of customers who were more or less likely to churn, develop a model for predicting churn rate based on those attributes, and leave with both recommendations for Telco company and predictions of churn rate for a list of customers (delivered via csv). 

## Initial Questions

1. Is the churn rate effected by monthly charges?

2. Does churn rate related to tenure?

3. Does the churn rate related to the additional services?

4. Does the churn rate effeted by contract type?



## Data Dictionary

Variables are used in this analysis: 

* churn
* monthly charges
* tenure
* contract types: month-to-month, one-year, two-year
* additional services: online security, online backup, tech support, streaming tv, streaming movies


## Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the telco_churn table. Store that env file locally in the repository.
2. Clone my repo (including the acquire_telco.py and prepare_telco.py) (confirm .gitignore is hiding your env.py file)
3. Libraries used are pandas, matplotlib, seaborn, numpy, sklearn.
4. You should be able to run telco_churn_report.

## Plan

### Wrangle

Modules (acquire.py + prepare.py)

1. Test acquire function
2. Add to acquire.py module
3. Write code to clean data in notebook
4. Merge code into a single function & test
5. Write code to split data in notebook
6. Merge code into a single function & test
7. Merge functions in a single function & test
8. Add all 3 functions (or more) to prepare.py file
9. Import into notebook and test functions

### Missing Values (report.ipynb)

There are 11 missing value for total charge. Since 11 rows is a very small portion of the whole data set, so I just dropped it.

### Data Split (prepare.py (def function), report.ipynb (run function))

* train = 56%
* validate = 24%
* test = 20%

### Using your modules (report.ipynb)

once acquire.py and prepare.py are created and tested, import into final report notebook to be ready for use.

### Set the Data Context

1. Overall churn rate
* run train.shape to show the data rows and columns inforamtion (4500,55)
* run train.churn.value_counts() to show the number for churn
* plot a hist chart, x is churn, y is churn count

2. churn rate by service type
* run pd.crosstab to show the percentage of each service type
* plot a hist chart, x is service type, y is churn count

3. churn rate by contract type
* run pd.crosstab to show the percentage of each contract type
* plot a hist chart, x is contract type, y is churn count

### Explore

1. Is the churn rate effected by monthly charges?
2. Does churn rate related to tenure?
3. Does the churn rate related to the additional services?
4. Does the churn rate effeted by contract type?

### Exploring through visualizations (report.ipynb)

1. Is the churn rate effected by monthly charges?
* what is the mean for chun and non-churn customers? plot a boxplot to show the differece between each group, x is churn, y is monthly charges
* what is the distribution looks like? plot a kdeplot to visualize change of churn with monthly charges, x is monthly charge, y is density.
* run a t-test (2 samples 1-tailed) on monthly charge and churn

2. Does churn rate related to tenure?
* what is the mean difference of tenure between churn and non-churn? plot a boxplot for tenure and churn, x is churn, y is tenure.
* use groupby to see the mean of churn and non-churn
* run a t-test (2 samples 1-tailed) on tenure and churn

3. Does the churn rate related to the additional services?
* what is the churn difference between additional service numbers? plot a countplot, x is addtional service number use, y is churn count.

4. Does the churn rate effeted by contract type?
* crosstab contract type and churn
* what is the difference between different contrat types? plot a countplot, x is contract type, y is churn count.

### Summary (report.ipynb)

1. Customers who have high monthly charges are more like to churn.
2. The churn customers have less tenure.
3. The more additional services use, the churn rate is lower.
4. Month-to-month contract type has higher churn rate.

Therefore, features I will use are: 
* monthly charges
* tenure
* addtional services
* contracts type

## Modeling

### Select Evaluation Metric (Report.ipynb)
Here I will use accuracy as my metric to evalute my models.

### Evaluate Baseline (Report.ipynb)
The baseline I set for train set is the mode of churn (churn = 0).

### Develop 3 Models (Report.ipynb)
* Decision tree
* KNN
* Logistic regression

### Evaluate on Train (Report.ipynb)

### Evaluate on Validate (Report.ipynb)

### Evaluate Top Model on Test (Report.ipynb)
The top model is logistic regression.


## Report (Final Notebook)

### code commenting (Report.ipynb)

### Written Conclusion Summary (Report.ipynb)

### conclusion recommendations (Report.ipynb)

### conclusion next steps (Report.ipynb)

### no errors (Report.ipynb)

## Live Presentation

### Intro (live)

### audience & setting (live)

### content (live)

### Verbal Conclusion (findings, next steps, recommendations) (live)

### time (live)

## Deliver Predictions
Deliver predictions with telco_churn_prediction.csv.
