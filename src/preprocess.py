# Libraries

import pandas as pd
import src.config as cf
from sklearn.preprocessing import MinMaxScaler

# Missing Values

def missing_values_prep(df):
    
    # Imputing numerical columns
    if cf.imputation_strategies['numerical'] == 'median':
        for col in cf.numerical_columns:
            median_value = df[col].median()
            df[col].fillna(median_value, inplace = True)
    
    # Imputing categorical columns
    if cf.imputation_strategies['categorical'] == 'mode':
        for col in cf.categorical_columns:
            mode_value = df[col].mode()[0]
            df[col].fillna(mode_value, inplace = True)
    
    return df

def encode_categorical_columns(df):
    # Encodes categorical columns. One-hot for nominals, mappings for binary/ordinals

    # Binary
    
  #  binary_mappings
    
   # for col in cf.binary_columns:
   #     df[col] =
   return 1
