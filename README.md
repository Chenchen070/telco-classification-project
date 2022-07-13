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

