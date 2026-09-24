import pandas as pd

def solution(df1, df2, df3):
    df_merged=df1.merge(df2,on='emp_id',how='inner')
    df_final=df_merged.merge(df3,on='emp_id',how='left')
    return df_final