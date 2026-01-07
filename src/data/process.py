import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(path: str):
    df = pd.read_csv(path)
    df = df.dropna()
    X = df.drop("Potability", axis=1)
    y = df["Potability"]
    return train_test_split(X, y, test_size=0.2, random_state=42)