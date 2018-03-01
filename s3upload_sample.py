import json
import boto3

bucket_name = "daigoiot"
img_file = "face1.jpg"

s3 = boto3.resource('s3')
s3.Bucket(bucket_name).upload_file('/home/pi/' + img_file, img_file)