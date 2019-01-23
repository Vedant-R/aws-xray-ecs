# Installing the dependencies
from aws_xray_sdk.core import xray_recorder
from time import sleep
import boto3

# Configuring xray recorder to send trace data to xray daemon
xray_recorder.configure(
    sampling=False,
    context_missing='LOG_ERROR',
    plugins=('EC2Plugin', 'ECSPlugin'),
    daemon_address='127.0.0.1:2000')

# Defining logic to create s3 bucket inside the xray capture decorator
@xray_recorder.capture('s3-bucket-function')
def create_s3_bucket():
    print('test message.')
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket='example-s3-bucket',
                     CreateBucketConfiguration={'LocationConstraint': '<your-region-name>'})

# Calling the logic function from main function
def main():
    xray_recorder.begin_segment('bucket creation')
    sleep(1)
    create_s3_bucket()
    sleep(1)
    xray_recorder.end_segment()


if __name__ == '__main__':
    main()

