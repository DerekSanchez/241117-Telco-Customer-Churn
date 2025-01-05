import pandas as pd
from importlib import import_module
from sklearn.model_selection import cross_val_score, GridSearchCV
from src.config import manual_hyperparameters, hyperparameter_grids, models, cv_folds
from src.preprocess import get_preprocessing_pipeline # OJOOO DEFINIR ESTO




def get_model