
import pandas as pd

# Set the API Endpoint URL
url = "https://data.cityofnewyork.us/api/views/ipu4-2q9a/rows.csv?accessType=DOWNLOAD"

# Read the dataset from the URL
df = pd.read_csv(url)

# Save the dataset to a CSV file
df.to_csv("data/DOB_Permit_Issuance.csv", index=False)
