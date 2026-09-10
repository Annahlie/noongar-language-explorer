from src.data_loader import load_data


data = load_data()

print("DATA VALIDATION REPORT")
print("----------------------")

print("Number of records:", len(data))
print("Columns:", list(data.columns))

print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())

print("\nDuplicate Noongar entries:")
print(data["noongar"].duplicated().sum())

print("\nFirst five records:")
print(data.head())