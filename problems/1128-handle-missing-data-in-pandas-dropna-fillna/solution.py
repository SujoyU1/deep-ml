import pandas as pd

def solution(df):
    df = df.copy()

    # 1. Keep columns with <= 50% missing
    df = df.loc[:, df.isna().mean() <= 0.5]

    # 2. Keep rows with <= 50% missing
    df = df.loc[df.isna().mean(axis=1) <= 0.5]

    # 3. Fill missing values
    numeric_cols = df.select_dtypes(include='number').columns
    non_numeric_cols = df.columns.difference(numeric_cols)

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    for col in non_numeric_cols:
        df[col] = df[col].fillna(df[col].mode().iloc[0])

    return df.reset_index(drop=True)