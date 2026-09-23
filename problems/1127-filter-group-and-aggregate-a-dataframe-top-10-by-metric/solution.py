import pandas as pd

def solution(df):
    df_new=df[df['status']=='completed']

    df_agg=df_new.groupby('region')['amount'].sum().reset_index()

    df_agg_sorted=df_agg.sort_values(by='amount',ascending=False)

    return df_agg_sorted.iloc[:10,:]

