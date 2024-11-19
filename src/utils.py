import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    """
    Loads a dataset from the specified path
    
    Parameters:
        path (str): path to the file
    
    Returns:
        pd.DataFrame: pandas dataframe loaded to python enviroment
    """
    return pd.read_csv(path)

def save_data(df, path):
    """
    Saves a dataset to the specified path
    
    Parameters:
        df (pd.DataFrame): dataset to save
        path (str): path to save to
    """
    df.to_csv(path, index = False)
    print(f"Data saved to {path}")

def save_plot(fig, filename):
    """
    Saves a plot to the specified path
    
    Parameters:
        fig (matplotlib.figure.figure): Figure to save
        filename (str): Path and file name to save the plot to
    """
    fig.savefig(filename)
    print(f"Gráfico guardado en: {filename}")
