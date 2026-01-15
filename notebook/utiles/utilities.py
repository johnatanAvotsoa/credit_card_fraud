import pandas as pd 

def load_data(directory) : 
    df = pd.read_csv(directory)
    return df 
    