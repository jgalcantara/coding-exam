import datetime
import pandas as pd
import glob
import os
from datetime import datetime, timedelta

BASEDIR =  "app/raw"

def read_csv(dir, json):
    joined_files = os.path.join(BASEDIR, dir, "*") 
    joined_list = glob.glob(joined_files) 
    df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
    if json:
        return df
    if dir == "transaction":
        df['transactionDatetime'] = pd.to_datetime(df['transactionDatetime'], format="%Y-%m-%d %H:%M:%S")
    return df

def get_transactionId(transactionId):
    df_txn = read_csv("transaction", True)
    df_prod = read_csv("reference", False)
    txn_df = df_txn[df_txn['transactionId'] == transactionId]
    prod_df = df_prod[df_prod['productId'] == txn_df['productId'].item()]
    resulting_df = pd.concat([txn_df.reset_index(drop=True), prod_df.reset_index(drop=True)], axis=1)[['transactionId', 'productName', 'transactionAmount', 'transactionDatetime']]
    return resulting_df

def transaction_products(last_n_days, col_summary):
    df_txn = read_csv("transaction", False)
    df_prod = read_csv("reference", False)
    start_date = datetime.now() - timedelta(days=last_n_days)
    df_date = df_txn[df_txn['transactionDatetime'] >= start_date]
    df_date = df_date.groupby('productId').agg({'transactionAmount': 'sum'}).reset_index()
    df_merge = pd.merge(df_date, df_prod, on='productId', how='inner')[[col_summary, 'transactionAmount']]
    if col_summary == 'productManufacturingCity':
        df_merge = df_merge.rename(columns={col_summary: 'cityName', 'transactionAmount': 'totalAmount'})
    else:
        df_merge = df_merge.rename(columns={'transactionAmount': 'totalAmount'})
    return df_merge

