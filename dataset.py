import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = 'Crop_recommendation.csv'  # Replace with the actual file path
dataset = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(dataset.head())