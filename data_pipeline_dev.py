import pandas as pd
import numpy as np
from datetime import datetime

# Step 1: Load data
def load_data(path):
    try:
        df = pd.read_csv(path)
        print(f"Data loaded successfully with {len(df)} records.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

# Step 2: Clean data
def clean_data(df):
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

# Step 3: Transform data
def transform_data(df):
    df['processed_date'] = datetime.now()
    if 'amount' in df.columns:
        df['amount'] = df['amount'].astype(float)
    return df

# Step 4: Save processed data
def save_data(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}.")
    except Exception as e:
        print(f"Error saving data: {e}")

# Main pipeline function
def run_pipeline(input_path, output_path):
    df = load_data(input_path)
    if df.empty:
        return
    df = clean_data(df)
    df = transform_data(df)
    save_data(df, output_path)

# Example usage
if __name__ == "__main__":
    run_pipeline("position_salaries.csv", "output_path.txt")