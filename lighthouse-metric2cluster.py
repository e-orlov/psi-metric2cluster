import pandas as pd
import numpy as np
from google.colab import files

# Upload CSV file
uploaded = files.upload()

# Load the uploaded CSV file
filename = list(uploaded.keys())[0]
df = pd.read_csv(filename, sep=';', encoding='utf-8')

# Convert comma decimal to dot and convert to float where needed
def convert_column(col):
    try:
        return df[col].str.replace(",", ".", regex=False).astype(float)
    except:
        return df[col]

for col in df.columns:
    if col != "Address":
        df[col] = convert_column(col)

# Define thresholds for each metric
thresholds = {
    'Largest Contentful Paint Time (ms)': {'good': 2500, 'poor': 4000},
    'Max Potential First Input Delay (ms)': {'good': 100, 'poor': 300},
    'Cumulative Layout Shift': {'good': 0.1, 'poor': 0.25},
    'First Contentful Paint Time (ms)': {'good': 1800, 'poor': 3000},
    'Speed Index Time (ms)': {'good': 3400, 'poor': 5800},
    'Time to Interactive (ms)': {'good': 3800, 'poor': 7300},
    'Total Blocking Time (ms)': {'good': 200, 'poor': 600},
    'Time to First Byte (ms)': {'good': 800, 'poor': 1800}
}

# Function to categorize each metric based on thresholds
def categorize(value, metric):
    if pd.isnull(value):
        return "No Data"
    if metric not in thresholds:
        return "No Threshold"
    good = thresholds[metric]['good']
    poor = thresholds[metric]['poor']
    if metric == 'Cumulative Layout Shift':
        if value <= good:
            return "Good"
        elif value <= poor:
            return "Needs Improvement"
        else:
            return "Poor"
    else:
        if value <= good:
            return "Good"
        elif value <= poor:
            return "Needs Improvement"
        else:
            return "Poor"

# Apply categorization to each metric
for metric in thresholds.keys():
    cluster_col = f"{metric} Cluster"
    df[cluster_col] = df[metric].apply(lambda x: categorize(x, metric))

# Display the resulting DataFrame
df.head()

# Save to new CSV
output_filename = "pagespeed_clustered.csv"
df.to_csv(output_filename, index=False)
files.download(output_filename)
