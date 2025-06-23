# etl_pipeline.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os

# ========== CONFIGURATION ==========
Input_file = 'raw_data.csv'
Output_file = 'processed_data.csv'
Target_column= 'target'  # replace with your actual target column name
# ===================================

def load_data(file_path):
    """Load raw data from CSV"""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Preprocess and transform the dataset"""
    # Separate features and target
    X = df.drop(columns=[Target_column])
    y = df[Target_column]

    # Identify numerical and categorical columns
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns

    # Define transformers
    numerical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine transformers
    preprocessor = ColumnTransformer([
        ('num', numerical_pipeline, numerical_cols),
        ('cat', categorical_pipeline, categorical_cols)
    ])

    # Fit and transform features
    X_processed = preprocessor.fit_transform(X)

    # Convert to DataFrame with feature names
    feature_names = preprocessor.get_feature_names_out()
    X_df = pd.DataFrame(X_processed.toarray() if hasattr(X_processed, 'toarray') else X_processed,
                        columns=feature_names)

    # Add target column back
    X_df[Target_column] = y.values

    return X_df

def save_data(df, Output_path):
    """Save the cleaned and transformed data"""
    df.to_csv(Output_path, index=False)
    print(f"Processed data saved to {Output_path}")

def main():
    if not os.path.exists(Input_file):
        print(f"Input file '{Input_file}' not found.")
        return

    print("Loading data")
    df = load_data(Input_file)

    print("Preprocessing data")
    processed_df = preprocess_data(df)

    print("Saving processed data to the .csv file")
    save_data(processed_df, Output_file)

    print("ETL pipeline process is completed")


if __name__ == "__main__":
    main()
