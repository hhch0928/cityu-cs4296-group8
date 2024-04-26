import csv
import boto3
from flask import Flask, request
from random import randint

app = Flask(__name__)

def generate_and_upload_numbers(count):
    # Create a list of random numbers between 1 and 10
    numbers = [randint(1, 10) for _ in range(count)]
    
    # Define CSV file name
    filename = 'numbers.csv'
    
    # Write numbers to CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number in numbers:
            writer.writerow([number])
    
    # Define S3 bucket and object key
    bucket_name = 'output-cs4296-ec2'
    key = 'numbers.csv'
    
    # Upload CSV file to S3
    s3 = boto3.client('s3')
    s3.upload_file(filename, bucket_name, key)
    
    return f'[EC2] Successfully generated {len(numbers)} random numbers and uploaded to S3.'

@app.route('/')
def index():
    return "This is the index page."

@app.route('/generate', methods=['GET'])
def generate_numbers():
    count = int(request.args.get('count', 1000000))  # Default count is 1000000 if not specified
    return generate_and_upload_numbers(count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
