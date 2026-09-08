import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def clean_data(df):
    df = df.copy()

    df['member_birth_year'] = df['member_birth_year'].mask(
        (df['member_birth_year'] < 1940) |
        (df['member_birth_year'] > 2001)
    )

    df['duration_min'] = df['duration_sec'] / 60

    df['member_age'] = 2019 - df['member_birth_year']

    return df