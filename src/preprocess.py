# ===============================
# Libraries and Configuration
# ===============================

# -------------------------------
# Path Setting
# -------------------------------

import sys
from pathlib import Path

project_root = Path().resolve().parent # set path to project root
sys.path.append(str(project_root))

# -------------------------------
# Libraries and Dependencies
# -------------------------------

import pandas as pd
import numpy as np
import src.config as cf
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import BaseEstimator, TransformerMixin

# -------------------------------
# Raise Error for Necessary Columns for Prep Step
# -------------------------------

class MissingColumnError(Exception):
    """
    Personalized exception for necessary columns in each step in preprocesssing.
    Raises an error if the column is not in the input data
    """
    def __init__(self, missing_columns):
        self.message = f"The following missing columns are missing: {', '.join(missing_columns)}"
        super().__init__(self.message)

# ===============================
# Feature Selection
# ===============================

class FeatureSelector(BaseEstimator, TransformerMixin):
    """
    Selects and drops irrelevant columns based on EDA analysis
    """
    
    def __init__(self):
        # optional attributes to store dropped columns
        self.dropped_features = None
    
    def fit(self, X, y = None):
        """
        Adjusts the class identifying the features to drop
        """
        # append lists of numerical and categorical features to drop
        self.dropped_features = cf.cat_features_to_drop + cf.num_features_to_drop
        
        return self
    
    def transform(self, X):
        """
        Drop irrelevant features from dataset
        """
        X_copy = X.copy()
        
        # verify if needed columns exist in data
        required_columns = self.dropped_features
        missing_columns = [col for col in required_columns if col not in X_copy.columns]

        if missing_columns:
            raise MissingColumnError(missing_columns)
        
        X_copy = X_copy.drop(columns = self.dropped_features, errors = 'ignore')
        
        return X_copy

# ===============================
# Data Cleaning
# ===============================

class DataCleaning(BaseEstimator, TransformerMixin):
    """
    Data Cleaning Class:
        - Data type adjustment
        - Handling inconsisting labels
        - Stadardize columns in inconsisten formatting
    """
    
    def __init__(self):
        pass
    
    def fit(self, X):
        """
        Fit Data Cleaning computations
        """
        return self
    
    def transform(self, X):
        X_copy = X.copy()
        
        required_columns = [
            'TotalCharges'
        ]
        
        missing_columns = [col for col in required_columns if col not in X_copy.columns]
        
        if missing_columns:
            raise MissingColumnError(missing_columns)
        
        # adjust data type
        X_copy['TotalCharges'] = pd.to_numeric(X_copy['TotalCharges'], errors = 'coerce')

        # adjust spaces in string columns
        object_columns = X_copy.select_dtypes(include = 'object').columns
        for col in object_columns:
            X_copy[col] = X_copy[col].str.strip()
    
        return X_copy


# ===============================
# Feature Engineering
# ===============================

class FeatureEngineering(BaseEstimator, TransformerMixin):
    """
    Feature Engineering including:
        - Creation of new columns
        - Transformation of existing columns
    """
    
    def __init__(self):
        pass
    
    def fit(self, X, y = None):
        """
        Fits any calculation to perform Feature Engineering
        """
        
        return self
    
    def transform(self, X):
        """
        Apply transformations and create new features
        """ 
        X_copy = X.copy()
        
        # verify if needed columns exist in data
        required_columns = [
            'tenure',
            'MonthlyCharges',
            'InternetService',
            'MultipleLines',
            'OnlineSecurity'
        ]
        missing_columns = [col for col in required_columns if col not in X_copy.columns]
        
        if missing_columns:
            raise MissingColumnError(missing_columns)
        
        # create new column: TotalCost
        X_copy['TotalCost'] = X_copy['tenure'] * X_copy['MonthlyCharges']
        
        # create new column: RevenueAdjustment
        X_copy['RevenueAdjustment'] = X_copy['TotalCharges'] - X_copy['TotalCost']
        
        # create new column: log monthly charges
        X_copy['LogMonthlyCharges'] = X_copy['MonthlyCharges'].apply(
            lambda x: np.log(x) if pd.notnull(x) and x > 0 else 0)
        
        # column values simplification: InternetService
        X_copy['InternetService'] = X_copy['InternetService'].replace(
            {'Fiber optic': 'Yes',
             'DSL' : 'Yes'}
            )
        
        # column values simplification: MultipleLines
        X_copy['MultipleLines'] = X_copy['MultipleLines'].replace(
            {'No phone service': 'No'}
            )
        
        # column values simplification: OnlineSecurity
        X_copy['OnlineSecurity'] = X_copy['OnlineSecurity'].replace(
            {'No internet service': 'No'}
            )
        
        return X_copy

# ===============================
# Outlier Detection
# ===============================

class OutlierDetector(BaseEstimator, TransformerMixin):
    """
    Outlier detection based on Inter Quartile Range (IQR)
    - Identifies values outside the range defined by the threshold
    - allows the user to identify or eliminate outliers
    """
    
    def __init__(self, multiplier = 1.5 , action = 'remove'):
        """
        Parameters:
            multiplier (float): multiplier for IQR. default is 1.5
            action (str): defines what to do with the outlier:
                - 'remove' to delete them
                - 'cap' to cap them
                - 'flag' to flag them  
        """
        self.multiplier = multiplier
        self.action = action

    def fit(self, X, y = None):
        """
        Fits necessary statisctis (mean and sd)
        """
        numerical_cols = X.select_dtypes(include = ['int64', 'float64']).columns
        self.q1 = X[numerical_cols].quantile(0.25)
        self.q3 = X[numerical_cols].quantile(0.75)
        self.iqr = self.q3 - self.q1 
        
        # compute limits
        self.lower_bound = self.q1 - self.multiplier * self.iqr
        self.upper_bound = self.q3 + self.multiplier * self.iqr
        
        return self
    
    def transform(self, X):
        """
        Applies outlier detection and handling as specified
        """
        X_copy = X.copy()
        
        # select numerical columns
        numeric_cols = X_copy.select_dtypes(include = ['int64', 'float64']).columns
        
        # raise error if not in the dataset
        required_columns = numeric_cols
        missing_columns = [col for col in required_columns if col not in X_copy.columns]
        
        if missing_columns:
            raise MissingColumnError(missing_columns)
        
        # identify outliers
        outliers = (X_copy[numeric_cols] < self.lower_bound) | (X_copy[numeric_cols] > self.upper_bound)
        
        if self.action == 'remove':
            # remove rows with outliers
            X_copy = X_copy[~outliers.any(axis = 1)]
            
        elif self.action == 'cap':
            # cap values
            X_copy[numeric_cols] = X_copy[numeric_cols].clip(self.lower_bound, self.upper_bound, axis = 1)
        
        elif self.action == 'flag':
            # create a column indicating the presence of outliers
            X_copy['outlier_flag'] = outliers.any(axis = 1)
        
        return X_copy
            
         
        
        
        
# ===============================
# Missing Values Handling
# ===============================

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

# ===============================
# Encoding Categorical Nominal
# ===============================

def encode_categorical_columns(df):
    # Encodes categorical columns. One-hot for nominals, mappings for binary/ordinals

    # Binary
    
  #  binary_mappings
    
   # for col in cf.binary_columns:
   #     df[col] =
   return 1

# ===============================
# Encoding Categorical Binary
# ===============================

# ===============================
# Encoding Categorical Ordinal
# ===============================

# ===============================
# Data Augmentation
# ===============================



