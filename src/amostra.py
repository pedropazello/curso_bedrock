import boto3

# Cria o cliente Bedrock
bedrock = boto3.client(service_name='bedrock', region_name='us-east-1')

# Lista os modelos fundacionais disponíveis
models = bedrock.list_foundation_models()

# Exibe os modelos listados
print(models)
