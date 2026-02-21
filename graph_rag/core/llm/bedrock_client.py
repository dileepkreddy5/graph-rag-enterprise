import boto3
import json
import os


class BedrockClient:
    def __init__(self):
        self.region = os.getenv("AWS_REGION", "us-east-1")
        self.model_id = os.getenv(
            "BEDROCK_MODEL_ID",
            "anthropic.claude-3-sonnet-20240229-v1:0"
        )

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=self.region
        )

    def generate(self, prompt: str, max_tokens: int = 500):

        body = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt}
                    ]
                }
            ],
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens
        }

        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body)
        )

        response_body = json.loads(response["body"].read())

        return response_body["content"][0]["text"]
