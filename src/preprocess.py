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
import src.config as cf
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import BaseEstimator, TransformerMixin

# -------------------------------
# Raise Error for Necessary Columns
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
        X_copy = X_copy.drop(columns = self.dropped_features, errors = 'ignore')
        
        return X_copy

# ===============================
# Data Cleaning
# ===============================


# ===============================
# Feature Engineering
# ===============================

class FeatureEgineering(BaseEstimator, TransformerMixin):
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
        required_columns = []
        missing_columns = [col for col in required_columns if col not in X_copy.columns]
        
        if missing_columns:
            raise MissingColumnError(missing_columns)
        
        # create new column: TotalCost
        X_copy['TotalCost'] = X_copy['tenure'] * X_copy['MonthlyCharges']
        
        # create new column: RevenueAdjustment
        X_copy['RevenueAdjustment'] = X_copy['TotalCharges'] - X_copy['TotalCost']
        
        


# ===============================
# Outlier Detection
# ===============================


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




# ===============================
# Test Block
# ===============================

if __name__ == "__main__":
    import pandas as pd
    import src.config as cf

    # Crear un ejemplo de DataFrame para pruebas
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': ['A', 'B', 'C'],
        'feature4': ['X', 'Y', 'Z'],
        'target': [0, 1, 0]
    }
    df = pd.DataFrame(data)

    # Definir listas en config temporalmente para prueba
    cf.num_features_to_drop = ['feature1', 'feature2']
    cf.cat_features_to_drop = ['feature3']

    # Probar la clase FeatureSelector
    selector = FeatureSelector()
    selector.fit(df)
    transformed_df = selector.transform(df)

    print("Original DataFrame:")
    print(df)
    print("\nDataFrame después de Feature Selection:")
    print(transformed_df)