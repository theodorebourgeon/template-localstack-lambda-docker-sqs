# SQS
## Create
awslocal sqs create-queue --queue-name test-lambda-queue
## List
awslocal sqs list-queues
## Send message 
awslocal sqs send-message --queue-url http://localhost:4566/000000000000/test-lambda-queue --message-body "This is a test"

# Lambda 
## Create 
awslocal lambda create-function --function-name test-lambda --code ImageUri=test-lambda:latest --role arn:aws:iam::000000000:role/lambda-ex
## Invoke
awslocal lambda invoke --function-name arn:aws:lambda:us-east-1:000000000000:function:test-lambda response.json
## Update
awslocal lambda update-function-code --function-name test-lambda --image-uri test-lambda:latest
## List
awslocal lambda list-functions
## Bind to SQS
awslocal lambda create-event-source-mapping --function-name test-lambda --batch-size 1 --event-source-arn arn:aws:sqs:us-east-1:000000000000:test-lambda-queue


