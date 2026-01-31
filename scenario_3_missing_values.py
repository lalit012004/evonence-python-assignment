import pandas as pd

def handle_missing_income(df):
    skewness = df["income"].skew()
    if abs(skewness) <= 0.5:
        value = df["income"].median()
    else:
        value = df["income"].mode()[0]
    df["income"] = df["income"].fillna(value)
    return df
