import re

def clean_text_column(df, column_name):
    df[column_name] = df[column_name].str.lower()
    df[column_name] = df[column_name].apply(
        lambda x: re.sub(r'[^a-z0-9\s]', '', x))
    df[column_name] = df[column_name].apply(lambda x: x.split())
    return df
