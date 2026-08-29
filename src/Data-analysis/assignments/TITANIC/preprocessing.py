import pandas as pd

def Read_data_file(file_path):
    """Load a CSV file into a DataFrame with basic error handling."""
    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        print("Error: File does not exist.")

    except Exception:
        print("Error: The file cannot be read.")

def Drop_unnecessary_features(df, cols_to_drop):
    """Drop specified columns from the DataFrame."""
    return df.drop(columns=cols_to_drop)

def Check_data_type(df):
    """Return a transposed summary of data types and unique value counts."""
    result = pd.DataFrame({
        "Dtype": df.dtypes,
        "Num_Unique": df.nunique()
    })
    return result.T