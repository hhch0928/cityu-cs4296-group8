import csv
import boto3
import os
import time
from random import randint

def lambda_handler(event, context):
    # Get the count of random numbers to generate from the query parameters
    count = int(event['queryStringParameters']['count'])
    
    # Create a list of random numbers between 1 and 10
    numbers = [randint(1, 10) for _ in range(count)]
    
    # Define CSV file name
    filename = '/tmp/numbers.csv'
    
    # Write numbers to CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number in numbers:
            writer.writerow([number])
    
    # Measure the time before initiating the upload to S3
    start_time = time.time()
    
    # Define S3 bucket and object key
    bucket_name = 'output-cs4296-lambda'
    key = 'numbers.csv'
    
    # Create an S3 client
    s3 = boto3.client('s3')
    
    # Calculate the time taken to connect to S3
    s3_connection_time = time.time() - start_time
    
    # Upload CSV file to S3
    start_time = time.time()  # Start measuring upload time
    s3.upload_file(filename, bucket_name, key)
    
    # Calculate the time needed to complete the upload
    upload_time = time.time() - start_time
    
    return {
        'statusCode': 200,
        'body': f'[Lambda] Successfully generated {len(numbers)} random numbers and uploaded to S3. \nS3 Connection Time: {s3_connection_time} seconds. \nUpload Time: {upload_time} seconds.'
    }
