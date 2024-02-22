import os
import boto3
import json

brt = boto3.client(service_name='bedrock-runtime', region_name='us-west-2')

def get_text_response(input_content): 
    
    body = {
        "prompt": input_content,
        "temperature": 0.5,
        "top_p": 0.9,
        "max_gen_len": 512,
    }

    model_id = 'meta.llama2-13b-chat-v1'
    response = brt.invoke_model(
        modelId=model_id, body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())
    completion = response_body["generation"]

    return completion
