import pandas as pd
import numpy as np
from google.colab import files

# Upload CSV file
uploaded = files.upload()

# Load with semicolon delimiter
filename = list(uploaded.keys())[0]
df = pd.read_csv(filename, sep=";")

# Convert comma decimal to dot and convert to float where needed
def convert_column(col):
    try:
        return df[col].str.replace(",", ".", regex=False).astype(float)
    except:
        return df[col]

for col in df.columns:
    if col != "Address":
        df[col] = convert_column(col)

# Function to create cluster labels based on quantiles
def cluster_column(column):
    q1 = column.quantile(0.33)
    q2 = column.quantile(0.66)
    def label(val):
        if val <= q1:
            return "Good"
        elif val <= q2:
            return "Needs Improvement"
        else:
            return "Poor"
    return column.apply(label)

# Create cluster columns
for col in df.columns:
    if col != "Address":
        cluster_col_name = f"{col} cluster"
        df[cluster_col_name] = cluster_column(df[col])

# Display the resulting DataFrame
df.head()

# Save to new CSV
output_filename = "pagespeed_clustered.csv"
df.to_csv(output_filename, index=False)
files.download(output_filename)
