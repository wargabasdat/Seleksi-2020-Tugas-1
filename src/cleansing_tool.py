import csv, json
import pandas as pd
from more_itertools import unique_everseen

def fixDate(csvFilename, newCsvFilename):
    df = pd.read_csv(csvFilename, encoding='utf-8')
    df['birth_date'] = df['birth_date'].str.replace('Jan.', 'January')
    df['birth_date'] = df['birth_date'].str.replace('Feb.', 'February')
    df['birth_date'] = df['birth_date'].str.replace('Aug.', 'August')
    df['birth_date'] = df['birth_date'].str.replace('Sept.', 'September')
    df['birth_date'] = df['birth_date'].str.replace('Oct.', 'October')
    df['birth_date'] = df['birth_date'].str.replace('Nov.', 'November')
    df['birth_date'] = df['birth_date'].str.replace('Dec.', 'December')
    df.to_csv(newCsvFilename, index=False, encoding='utf-8')

def cleanCurrency(csvFilename, newCsvFilename):
    df_orig = pd.read_csv(csvFilename, encoding='utf-8')
    df = df_orig.copy()
    df['value'] = df['value'].str.replace('.', '')
    df['value'] = df['value'].str.replace('€', '')
    df['wage'] = df['wage'].str.replace('.', '')
    df['wage'] = df['wage'].str.replace('€', '')
    df["value"] = pd.to_numeric(df["value"], downcast="float")
    df["wage"] = pd.to_numeric(df["wage"], downcast="float")
    df.to_csv(newCsvFilename, index=True, encoding='utf-8')

fixDate('FIFA_index_20.csv', 'clean_FIFA.csv')