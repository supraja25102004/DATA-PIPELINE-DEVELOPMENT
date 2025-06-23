# DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: ANKEPALLI SHIVA SUPRAJA

*INTERN ID*: CT08DN1734

*DOMAIN*: DATA SCIENCE

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

## ETL Pipeline Overview:

The ETL (Extract, Transform, Load) process commonly used in data preprocessing for machine learning projects. It takes a raw dataset in CSV format, cleans and transforms it using Scikit-learn pipelines, and saves a ready-to-use dataset for model training.

Extract: Get data from one or more sources (CSV, database, API).

Transform: Clean, filter, or enrich the data.

Load: Store the transformed data into a destination (CSV, database, etc.).

## Purpose:

Data preprocessing is a critical first step in any data science project. Raw datasets often contain:

1.Missing values

2.Inconsistent formats

3.Mixed data types (numerical and categorical)

To ensure the performance of machine learning models, data must be cleaned, standardized, and encoded properly. This ETL pipeline addresses all these tasks in a reproducible, automated
way.

## Pipeline Steps:

### Extract (Load the Data):

def load_data(file_path):

    return pd.read_csv(file_path)

Uses pandas to load raw data from a CSV file.

Assumes the input is located at raw_data.csv.

### Transform (Preprocess the Data):

def preprocess_data(df):

    ...

#### Key preprocessing steps performed:

*1.Splitting Features and Target:*

   The pipeline separates the feature set X from the target variable y (defined by Target_column).

*2.Data Type Detection:*

   Automatically identifies:

       Numerical columns (int64, float64)

       Categorical columns (object, category)

*3.Handling Missing Values:*

   Numerical columns: imputed using mean

   Categorical columns: imputed using most frequent

*4.Feature Scaling and Encoding:*

   Numerical columns: Standardized using StandardScaler

   Categorical columns: One-hot encoded using OneHotEncoder

*5.ColumnTransformer:*

   A powerful Scikit-learn tool used to apply different preprocessing strategies to different column types in parallel.

*6.Final Dataset Assembly:*

   All transformed features are combined into a new DataFrame.

   The original target column is appended back to make the dataset ready for training.

### Load (Save the Preprocessed Data):

def save_data(df, Output_path):

    df.to_csv(Output_path, index=False)

Saves the fully preprocessed dataset to processed_data.csv, enabling smooth transition into the modeling phase.

## How to use:

1.Place your raw dataset as raw_data.csv in the same folder.

2.Modify Target_column = 'target' to match your actual target variable name.

3.Open terminal/VS Code and run:

   python etl_pipeline.py

4.Check processed_data.csv for the output.

## Benefits of this project:

*1.Automated Preprocessing:*

   Reduces manual errors and ensures consistent data handling.

*2.Pipeline Structure:*

   Scikit-learn pipelines make the process modular and scalable.

*3.Model Readiness:*

   Output dataset is clean, numeric, and ready for ML model training.

*4.Reusable Code:*

   Can be used as a base for future datasets or added into a larger ML workflow.

*5.Handles Mixed Data Types:*

   Applies best practices for both numerical and categorical preprocessing.

## Why This ETL Pipeline is Important in Data Science:

1.In real-world data science projects:

   Raw data is almost never model-ready.

   Reproducibility and automation are essential.

   Preprocessing needs to be scalable, modular, and reusable across different projects.

2.This pipeline handles these issues by:

   Providing consistent preprocessing.

   Supporting both numerical and categorical features.

   Outputting a clean dataset usable by any ML model.

## OUTPUT:

![Image](https://github.com/user-attachments/assets/630dce51-ddb2-4223-9607-e2295c2c76eb)












