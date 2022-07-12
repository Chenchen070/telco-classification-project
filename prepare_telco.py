import acquire_telco
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import math

def clean_telco_data(df):
    df["total_charges"] = pd.to_numeric(df["total_charges"], errors="coerce")
    df = df.drop_duplicates()
    df = df.dropna() # drop 11 row that total charge are null
    df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'], inplace=True)
    
    # encode binary categorical variables into numeric values
    df['gender_encoded_(female=1)'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    df['online_security_bool'] = df.online_security.map({'Yes': 1, 'No': 0, 'No internet service': 0})
    df['online_backup_bool'] = df.online_backup.map({'Yes': 1, 'No': 0, 'No internet service': 0})
    
    # Get dummies for non-binary categorical variables
    df_dummy = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, drop_first=True)
    df = pd.concat([df, df_dummy],axis=1)
    
    # encode number_relationships by utilizing information from dependents_encoded and partner_encoded
    df['number_relationships'] = df['dependents_encoded'] + df['partner_encoded']

    # encode number_online_services by utilizing information from online_security_encoded and online_backup_encoded
    df['number_online_services'] = df['online_security_bool'] + df['online_backup_bool']

    # encode tenure in years (rounded down) by utilizing information from tenure (currently stored in months)
    df['yearly_tenure'] = df.tenure.apply(lambda x: math.floor(x/12))

    # encode has_internet
    df['has_internet'] = df.internet_service_type.apply(lambda x: 0 if x == 'None' else 1)

    # make another column for additional online services
    df['additional_services'] = (df[['online_security','online_backup', 'device_protection', 'tech_support', 'streaming_tv',
                                 'streaming_movies']] == 'Yes').sum(axis=1)


    return df


def split_telco_data(df):
    '''
    This function performs split on telco data, stratify churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.2, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test

def prep_telco_data(df):
    df = clean_telco_data(df)
    train, validate, test = split_telco_data(df)
    
    return train, validate, test