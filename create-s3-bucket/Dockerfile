# Base image
FROM python:3-alpine

# Installing dependencies
RUN pip install boto3 \
    && pip install aws-xray-sdk \
    && pip install tox

# Set your environment variables
ENV AWS_DEFAULT_REGION <your-region-name>
ENV IAM_ROLE <your-ecsInstanceRoleArn>

# Install and run application into container
RUN set -ex && mkdir /app
WORKDIR /app

COPY xray-test.py /app/create-s3-bucket.py

CMD ["python3", "create-s3-bucket.py"]
