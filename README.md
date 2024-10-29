## Lambda Proxy Integration 

This repository shows how to integrate with AWS lambda proxy integrations

## Prerequisites
* Docker and docker-compose


## Notes 

* Local may not work properly like headers may not be seen properly deploying it on the aws will work as expected

* ![image](https://github.com/user-attachments/assets/c04d97fe-0710-4ff2-819f-0f69ba2067e0)


## Steps  

* **Step 1**: Add your code and add all custom pip dependencies inside requirements.txt
* **Step 2**: Run below Command
    ``` bash 
        docker logout public.ecr.aws
        docker-compose up
    ```
* **Step 3**: Test Your code in localhost - 0.0.0.0:9003
```bash 
curl --location 'http://0.0.0.0:9003/2015-03-31/functions/function/invocations' \
--header 'Content-Type: application/json' \
--data '{
    "body": "{ \"get_response\": \"200\"}"
}'
```
* **Step 4**: Enjoy :wink:
