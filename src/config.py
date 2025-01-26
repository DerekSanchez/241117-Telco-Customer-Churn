
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
    'customerID',
    'Dependents',
    'Partner',
    'gender',
    'PhoneService',
    'MultipleLines'
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

test_size = 0.3
random_state = 123


# ===============================
# Models
# ===============================
  
models = {
    'RandomForest' : 'sklearn.ensemble.RandomForestClassifier',
    'GradientBoosting' : 'sklearn.ensemble.GradientBoostingClassifier',
    'LogisticRegression' : 'sklearn.linear_model.LogisticRegression',
    'SVM' : 'sklearn.svm.SVC'
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
    'LogisticRegression' : {
        'C' : uniform(0.01, 10),
        'penalty' : ['l1', 'l2', 'elasticnet', 'none'],
        'solver' : ['saga', 'liblinear'] 
    },
    'SVM' : {
        'C' : uniform(0.01, 10),
        'kernel' : ['lienar', 'poly', 'rbf', 'sigmoid'],
        'gamma' : uniform(0.001, 1),
        'probability' : True
    }
}

grid_param_distributions = {
    'RandomForest' : {
        'n_estimators' : [400, 427, 450],
        'max_depth' : [12, 17, 22],
        'min_samples_split' : [0.01, 0.015, 0.02],
        'min_samples_leaf' : [0.01, 0.015, 0.02]
    },
    'GradientBoosting' : {
        'learning_rate' : [0.01, 0.1],
        'n_estimators' : [100, 200],
        'max_depth' : [3, 5]
    },
    'LogisticRegression' : {
        'C' : [0.01, 0.1, 1, 10],
        'penalty' : ['l1', 'l2'],
        'solver' : ['liblinear', 'saga']   
    },
    'SVM' : {
        'C' : [0.01, 0.1, 1, 10],
        'kernel' : ['linear', 'rbf'],
        'gamma' : ['scale', 'auto', 0.001, 0.01, 0.1],
        'probability' : True
    }
}

manual_hyperparameters = {
    'RandomForest' : {
        'n_estimators': 427, 
        'max_depth' : 17, 
        'min_samples_split' : 0.014303,
        'min_samples_leaf': 0.015765
    },
    'GradientBoosting' : {
        'learning_rate' : 0.01, 
        'n_estimators' : 100, 
        'max_depth' : 4
    },
    'LogisticRegression' : {
        'C' : 5.20485,
        'penalty' : 'l1',
        'solver' : 'saga',
        'max_iter' : 500
    },
    'SVM' : {
        'C' : 1.0,
        'kernel' : 'rbf',
        'gamma' : 'scale',
        'probability' : True
    }
}

# -------------------------------
# Enviroment Hyperparameters
# -------------------------------

# cross-validation configuration
cv_folds = 10

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