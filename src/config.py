# Libraries

from pathlib import Path

# Paths

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

# Preprocessing

numerical_columns = [
    'tenure',
    'MonthlyCharges',
    'TotalCharges']

ordinal_columns = [
    'Contract'
]

binary_columns = [
    'gender',
    'Partner',
    'Dependents',
    'PhoneService',
    'PaperlessBilling',
    'Churn'
]

nominal_columns = [
    'InternetService',
    'PaymentMethod',
    'MultipleLines',
    'OnlineSecurity',
    'OnlineBackup',
    'DeviceProtection',
    'TechSupport',
    'StreamingTV',
    'StramingMovies'
]

categorical_columns = ordinal_columns + binary_columns + nominal_columns

binary_mappings = {
    'gender': {'Male': 1, 'Female': 0},
    'status': {'Active': 1, 'Inactive': 0},
    'PaperlessBilling': {'Yes': 1, 'No': 0}
}


# Missing Values Imputation

imputation_strategies = {
    
}


# Data split
test_size = 0.2
random_state = 123

# Plot configuration
plot_style = 'seaborn-darkgrid'
fig_size = (10, 6)