# Lambda image

## Build 
* docker-compose build test-lambda


## Test it locally
Run :
* docker run -p 9000:8080 test-lambda
* curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
* docker-compose down test-lambda

Everything is working fine ! 