import pandas as pd

# Read data from CSV file
df_csv = pd.read_csv('data/ICC Mens T20 Worldcup.csv')

# Print the entire DataFrame
print(df_csv)

# Printing DataFrame as a string (useful for large DataFrames)
print(df_csv.to_string())

# Displaying first few rows (head) and last few rows (tail)
print(df_csv.head())  # Default displays first 5 rows
print(df_csv.tail())  # Default displays last 5 rows

# Summary statistics of numerical columns
print(df_csv.describe())

# Displaying first 20 rows
print(df_csv.head(20))

# Information about the DataFrame, including column data types and memory usage
print(df_csv.info())

# Accessing a specific column (make sure column name is correct)
print(df_csv['Player Of The Match'])

# Accessing specific rows of a column
print(df_csv['Player Of The Match'][:10])  # First 10 rows

# Accessing multiple columns (make sure column names are correct)
print(df_csv[['Date', 'Player Of The Match']])