#pip install s3fs

# pip install 
import boto3 
import pandas as pd 
#create client object 
client = boto3.client('s3')

#give path 
path = 's3://name-of-bucket/nameoffile.csv'
df = pd.read_csv(path)
df.head()