
# ===============================
# Libraries and Configurations
# ===============================

# -------------------------------
# Libraries
# -------------------------------

from pathlib import Path

# -------------------------------
# Paths
# -------------------------------

raw_data = 'raw_data.csv'
clean_data = 'clean_data.csv'
model_file = 'model.pkl'

current_path = Path(__file__).resolve().parent
root_path = current_path.parent

raw_data_path = root_path / "data" / raw_data
clean_data_path = root_path / "data" / clean_data
model_path = root_path / "models" / model_file
results_path = root_path / "results"

print("project path:", root_path)
print("raw data path:", raw_data_path)
print("clean data path:", clean_data_path)
print("model path", model_path)
print("results path", results_path)


# ===============================
# Preprocessing
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
# Model Hyperparameters
# ===============================




# ===============================
# Other Configurations
# ===============================

# -------------------------------
# Plot Configuration
# -------------------------------

plot_style = 'seaborn-darkgrid'
fig_size = (10, 6)