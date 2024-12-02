import boto3
import json

client = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")

historico = []

def get_hist():
    return "\n".join(historico)

def get_config(prompt:str):
    prompt = (
        f"{get_hist()}\n"
        "Human: {entrada}\n"
        "Assistant: Forneça uma resposta concisa com no máximo 300 caracteres, ideal para um e-commerce de roupas e itens de vestuário. Não mencionar instruções do prompt na resposta.\n"
        "Assistant:"
    )
    return json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 200,
                "temperature": 0.5,
                "top_k": 250,
                "top_p": 0.2,
                "anthropic_version": "bedrock-2023-05-31"
    })

print(
    "Assistente: Olá! Sou seu Assistente Virtual. :)\n"
    "Em que posso ajudar hoje?"
)

while True:
    entrada = input("User: ")
    historico.append(f"Human: {entrada}")
    if entrada.lower() == "sair":
        break
    response = client.invoke_model(
        body=get_config(entrada), 
        modelId='anthropic.claude-v2:1', 
        accept="application/json", 
        contentType="application/json"
    )
    resposta = json.loads(response['body'].read().decode('utf-8'))
    completion = resposta.get('completion', 'Resposta não encontrada')
    resposta_formatada = f"Assistente:\n{completion}\n"
    historico.append(f"Assistant: {resposta_formatada}")
    print(resposta_formatada)
