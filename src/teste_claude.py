import boto3
import json

# Cria o cliente Bedrock
client = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")

# ID do modelo Claude v2.1
claude_model_id = 'anthropic.claude-v2:1'

# Configura a requisição para o modelo
claude_config = json.dumps({
    "prompt": "Human: Opções de sandália para uma caminhada na praia. Assistant:",
    "max_tokens_to_sample": 200,
    "temperature": 0.5,
    "top_k": 250,
    "top_p": 0.2,
    "anthropic_version": "bedrock-2023-05-31"
})

# Envia a requisição
response = client.invoke_model(
    body=claude_config,
    modelId=claude_model_id,
    accept="application/json",
    contentType="application/json"
)

# Processa a resposta
resposta = json.loads(response['body'].read().decode('utf-8'))
completion = resposta.get('completion', 'Resposta não encontrada')
resposta_formatada = f"Resposta:\n{completion}\n"
print(resposta_formatada)
