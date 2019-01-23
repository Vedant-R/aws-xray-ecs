# aws-xray-ecs

Implementing AWS X-Ray monitoring with AWS ECS

## What is AWS X-Ray?

AWS X-Ray is a service that collects data about requests that your application serves, and provides tools you can use to view, filter, and gain insights into that data to identify issues and opportunities for optimization. For any traced request to your application, you can see detailed information not only about the request and response, but also about calls that your application makes to downstream AWS resources, microservices, databases and HTTP web APIs.

The X-Ray SDK provides:

- Interceptors to add to your code to trace incoming HTTP requests

- Client handlers to instrument AWS SDK clients that your application uses to call other AWS services

- An HTTP client to use to instrument calls to other internal and external HTTP web services

The SDK also supports instrumenting calls to SQL databases, automatic AWS SDK client instrumentation, and other features.

For more information AWS X-Ray: [AWS X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

For more information on AWS X-Ray SDK (Github): [AWS X-Ray Github SDK](https://github.com/aws/aws-xray-sdk-python#trace-aiohttp-client-requests)

## Requirements

- Python3.x
- Docker
- AWS Services: X-Ray, ECS, ECR, S3, IAM

## Steps

The workflow here is to create a S3 bucket and capture the logs of successful creation on X-Ray Console. The xray-daemon-sdk lives in the code logic which send traces to 2000 port on which xray daemon listens and then displays the traces on the X-Ray Console. The codebase logic and the xray daemon are wrapped in a docker container, saved on ECR and is called through docker image from the ECR registry. This final step is done through ECS task definition.

- Create a python script to create a S3 bucket
- Create a Docker image of xray daemon and upload to ECR
- Create a Docker image of logic which includes the python file which creates the S3 bucket and upload to ECR
- Run the application through ECS Task Definition

## Output

- Service Map

![Screenshot of the AWS X-Ray console service map](/images/service-map.png?raw=true)

- Traces

![Screenshot of the AWS X-Ray console traces](/images/traces.png?raw=true)