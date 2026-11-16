# CSV Data Parsing and Cleaning Guidelines

This document outlines the standard steps and rules for cleaning and parsing CSV data using Python.

## Steps for Parsing and Cleaning CSV Data

1. **Import Required Libraries**
   Use standard libraries like `csv` or powerful data manipulation libraries like `pandas`.
   ```python
   import pandas as pd
   ```

2. **Load the CSV File**
   Read the CSV file into a DataFrame or standard reader, handling potential encoding issues (e.g., `utf-8`, `latin1`).
   ```python
   df = pd.read_csv('data.csv', encoding='utf-8')
   ```

3. **Inspect the Data**
   Check for missing values, incorrect data types, and structural anomalies.
   ```python
   print(df.info())
   print(df.head())
   ```

4. **Handle Missing Values**
   - Drop rows/columns with critical missing data, or fill them with appropriate defaults (mean, median, or placeholder).
   ```python
   df = df.dropna(subset=['critical_column'])
   df['optional_column'] = df['optional_column'].fillna('Unknown')
   ```

5. **Clean Data Fields**
   - Strip whitespace from string columns.
   - Standardize date formats.
   - Convert numeric columns to appropriate types (`int`, `float`).
   ```python
   df['text_column'] = df['text_column'].str.strip().str.lower()
   df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')
   df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')
   ```

6. **Remove Duplicates**
   Identify and remove duplicate rows to ensure data integrity.
   ```python
   df = df.drop_duplicates()
   ```

7. **Export Cleaned Data**
   Save the processed data to a new CSV file without the index.
   ```python
   df.to_csv('cleaned_data.csv', index=False)
   ```
