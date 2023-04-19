import requests
import boto3

# Download the dataset
url = "https://data.cityofnewyork.us/resource/ipu4-2q9a.json"
response = requests.get(url)
data = response.content

# Upload the file to S3
bucket_name = "permit-issuance"
filename = "raw.json"

s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
bucket.put_object(Key=filename, Body=data)
