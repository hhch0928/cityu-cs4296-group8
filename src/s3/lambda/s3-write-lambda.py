import csv
import boto3
import os
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
            
    # Define S3 bucket and object key
    bucket_name = 'output-cs4296-lambda'
    key = 'numbers.csv'
    
    # Upload CSV file to S3
    s3 = boto3.client('s3')
    s3.upload_file(filename, bucket_name, key)
    
    return {
        'statusCode': 200,
        'body': f'[Lambda] Successfully generated {len(numbers)} random numbers and uploaded to S3.'
    }
