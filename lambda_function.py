import boto3
import json
import os

# Initialize the Bedrock Runtime
# Ensure you have permissons for bedrock:InvokeModel in your IAM role
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    """
    AWS Lambda Handler for DataWhisperer.
    Expects 'query' and 'csv_header' in the event body.
    """
    try:
        # 1. Parse Input
        body = json.loads(event.get('body', '{}'))
        query = body.get('query')
        csv_header = body.get('csv_header')
        
        if not query or not csv_header:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing query or csv_header'})
            }

        # 2. Construct Prompt for Bedrock
        # We use Claude 3 Haiku for speed and cost-efficiency
        prompt_config = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"You are a Data Analyst Assistant. "
                        f"Here is the header of a CSV dataset: {csv_header}\n\n"
                        f"User Question: {query}\n\n"
                        f"Provide a concise answer or python pandas code to answer this."
                    )
                }
            ]
        }

        # 3. Invoke Bedrock
        model_id = "anthropic.claude-3-haiku-20240307-v1:0"
        
        response = bedrock.invoke_model(
            body=json.dumps(prompt_config),
            modelId=model_id,
            accept="application/json",
            contentType="application/json"
        )

        # 4. Parse Response
        response_body = json.loads(response.get('body').read())
        ai_reply = response_body['content'][0]['text']

        return {
            'statusCode': 200,
            'body': json.dumps({'answer': ai_reply})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }

if __name__ == "__main__":
    # Local Test Payload
    test_event = {
        "body": json.dumps({
            "query": "Calculate average sales.",
            "csv_header": "Date,Product,Sales,Region"
        })
    }
    print("Running local test...")
    try:
        result = lambda_handler(test_event, None)
        print("Result:", json.dumps(result, indent=2))
    except Exception as e:
        print(f"Local execution failed (likely due to missing AWS credentials): {e}")
