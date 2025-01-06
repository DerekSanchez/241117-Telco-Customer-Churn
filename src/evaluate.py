import json
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    f1_score,
    precision_score,
    recall_score,
    classification_report
)

from src.config import scoring_methods, scoring_mode, paths

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model on the test set
    
    Parameters:
        - model: Trained Model
        - X_test (pd.DataFrame): Test set (Features)
        - y_test (pd.Series) : Test set (Target)
    
    Returns:
        - dict: Dictionary with evaluation metrics
    """
    
    # predict on the test set
    y_pred = model.predict(X_test)
    
    # dynamyc selection of main score metric
    scoring = scoring_methods[scoring_mode]
    if scoring == 'roc_auc':
        score = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    elif scoring == 'f1':
        score = f1_score(X_test, y_test)
    elif scoring == 'precision':
        score = precision_score(X_test, y_test)
    elif scoring == 'recall':
        score = recall_score(X_test, y_test)
    else: # default to accuracy
        score = accuracy_score(X_test, y_test)
        
    # complete classificaton report
    report = classification_report(y_test, y_pred, output_dict = True)
    
    # consolidated results
    results = {
        'primary score' : {
            'metric' : scoring,
            'value' : score   
        },
        'classification_report' : report
    }
    
    return results

def save_metrics(metrics, model_name):
    """
    Saves testing metrics on a JSON file
    
    Parameters:
        - metrics (dict): Testing results
        - model_name (str): Name of evaluated model
    """
    # path to save metrics OJOOO DEFINIR ESTO YA
    metrics_path = None
    
    with open(metrics_path, 'w') as file:
        json.dump(metrics, file, indent = 4)
    
    print(f'Metrics saved on {metrics_path}')

    