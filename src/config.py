
# ===============================
# Libraries and Configurations
# ===============================

# -------------------------------
# Libraries
# -------------------------------

from pathlib import Path
from scipy.stats import randint, uniform

# -------------------------------
# Paths
# -------------------------------

raw_data = 'raw_data.csv'
clean_data = 'clean_data.csv'
model_file = 'model.pkl'

current_path = Path(__file__).resolve().parent
root_path = current_path.parent

paths = {
    # folders
    'data' : root_path / 'data',
    'notebooks' : root_path / 'notebooks',
    'results' : root_path / 'results',
    'models' : root_path / 'models',
    'source' : root_path / 'src',
    # specific files
    'data_raw' : root_path / 'data' / 'raw_data.csv',
    'model' : root_path / 'models' / 'model.pkl',
    'logs' : root_path / 'results' / 'log.txt'   
}

print("project path:", root_path)
print("raw data path:", paths['data_raw'])
print("model path", paths['model'])
print("results path", paths['results'])


# ===============================
# Target Preprocessing
# ===============================

# -------------------------------
# Encoding
# -------------------------------

target_mapping = {
    'Yes' : 1,
    'No': 0
}

# ===============================
# Feature Preprocessing
# ===============================



# -------------------------------
# Feature Selection
# -------------------------------

num_features_to_drop = [
    
]

cat_features_to_drop = [
    
]

# -------------------------------
# Missing Values Handling
# -------------------------------

imputation_strategies = {
    "numerical" : "median",
    "categorical" : "mode"
}

# -------------------------------
# Encoding
# -------------------------------

binary_mappings = {
    'gender': {'Male' : 1, 'Female' : 0},
    'partner': {'Yes' : 1, 'No' : 0},
    'dependents' : {'Yes' : 1, 'No' : 0},
    'PhoneService' : {'Yes' : 1, 'No' : 0},
    # not originally binary, but modified to be in Feature Engineering
    'MultipleLines' : {'Yes' : 1, 'No' : 0},
    'InternetService' : {'Yes' : 1, 'No' : 0},
    'OnlineSecurity' : {'Yes' : 1, 'No' : 0},
    'PaperlessBilling': {'Yes': 1, 'No': 0},
    'Churn': {'Yes' : 1, 'No' : 0}
}

ordinal_mappings = {
    'Contract':{
        'Month-to-month': 0,
        'Two year': 1,
        'One year': 2
    }
}

nominal_columns = [
    'PaymentMethod', 
    'OnlineBackup',
    'DeviceProtection',
    'TechSupport',
    'StreamingTV',
    'StreamingMovies',
    ]



# -------------------------------
# Data Split
# -------------------------------

test_size = 0.2
random_state = 123


# ===============================
# Models
# ===============================
  
models = {
    'RandomForest' : 'sklearn.ensemble.RandomForestClassifier',
    'GradientBoosting' : 'sklearn.ensemble.GradientBoostingClassifier'
}

# ===============================
# Hyperparameters
# ===============================

# -------------------------------
# Model Hyperparameters
# -------------------------------

random_param_distributions = {
    'RandomForest' : {
        'n_estimators' : randint(50, 500),
        'max_depth' : randint(5, 30),
        'min_samples_split' : uniform(0.01, 0.1),
        'min_samples_leaf' : uniform(0.01, 0.1)
        },
    'GradientBoosting' : {
        'learning_rate' : uniform(0.01, 0.2),
        'n_estimators' : randint(100, 300),
        'max_depth' : randint(3, 15)
    },
}

grid_param_distributions = {
    'RandomForest' : {
        'n_estimators' : [100, 200, 300],
        'max_depth' : [10, 15, 20],
        'min_samples_split' : [0.05, 0.1],
        'min_samples_leaf' : [0.02, 0.05]
        },
    'GradientBoosting' : {
        'learning_rate' : [0.01, 0.1],
        'n_estimators' : [100, 200],
        'max_depth' : [3, 5]
    },
}

manual_hyperparameters = {
    'RandomForest' : {
        'n_estimators': 100, 
        'max_depth' : 10, 
        'min_samples_split' : 5},
    'GradientBoosting' : {
        'learning_rate' : 0.1, 
        'n_estimators' : 200, 
        'max_depth' : 5},     
}

# -------------------------------
# Enviroment Hyperparameters
# -------------------------------

# cross-validation configuration
cv_folds = 5

# optimization scoring
scoring_methods = {
    'balanced' : 'roc_auc',
    'default' : 'accuracy'
}

scoring_mode = 'balanced'


# ===============================
# Other Configurations
# ===============================

# -------------------------------
# Plot Configuration
# -------------------------------

plot_style = 'seaborn-darkgrid'
fig_size = (10, 6)