import csv
import boto3
from flask import Flask, request
from random import randint
from datetime import datetime
import time

app = Flask(__name__)

def generate_and_upload_numbers(count):
    # Create a list of random numbers between 1 and 10
    numbers = [randint(1, 10) for _ in range(count)]
    
    # Define current datetime
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define CSV file name with current datetime
    filename = f'numbers_{current_datetime}.csv'
    
    # Write numbers to CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number in numbers:
            writer.writerow([number])
    
    # Measure the time before initiating the upload to S3
    start_time = time.time()
    
    # Define S3 bucket and object key with current datetime
    bucket_name = 'output-cs4296-ec2'
    key = filename
    
    # Upload CSV file to S3
    s3 = boto3.client('s3')
    
    # Calculate the time needed to connect to S3
    s3_connection_time = time.time() - start_time

    s3.upload_file(filename, bucket_name, key)
    
    # Calculate the time needed to complete the upload
    upload_time = time.time() - start_time
    
    return f'[EC2] Successfully generated {len(numbers)} random numbers and uploaded to S3 with filename: {key}. \nS3 Connection Time: {s3_connection_time} seconds.\nUpload Time: {upload_time} seconds.'

@app.route('/')
def index():
    return "This is the index page."

@app.route('/generate', methods=['GET'])
def generate_numbers():
    count = int(request.args.get('count', 1000000))  # Default count is 1000000 if not specified
    return generate_and_upload_numbers(count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
