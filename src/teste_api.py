import boto3
import json

client = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")
claude_model_id = 'anthropic.claude-v2:1'

claude_config = json.dumps({
    "prompt": "Human: Quais são as melhores opções de sandálias para uma caminhada na praia?\n"
    "Assistant: Forneça uma resposta concisa com no máximo 300 caracteres, ideal para um e-commerce de roupas e itens de vestuário. Não mencionar instruções do prompt na resposta."
    "Assistant:",
                "max_tokens_to_sample": 200,
                "temperature": 0.5,
                "top_k": 250,
                "top_p": 0.2,
                "anthropic_version": "bedrock-2023-05-31"
})

response = client.invoke_model(
    body=claude_config,
    modelId=claude_model_id,
    accept="application/json",
    contentType="application/json" 
)

resposta = response['body'].read().decode('utf-8')
print("Resposta:")
print(resposta)
