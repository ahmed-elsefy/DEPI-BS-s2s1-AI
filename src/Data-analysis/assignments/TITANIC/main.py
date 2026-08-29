"""Execute the Titanic data preprocessing and quality inspection pipeline."""
from preprocessing import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type
)

from Config.Config import cols_to_drop

df = Read_data_file("Titanic.csv")

if df is not None:

    print("Dataset loaded successfully.")
    print("\nFirst 5 rows:")
    print(df.head())

    df = Drop_unnecessary_features(df, cols_to_drop)

    print("\nDataset after removing unnecessary features:")
    print(df.head())
    print("\nData Quality Report:")
    print(Check_data_type(df))