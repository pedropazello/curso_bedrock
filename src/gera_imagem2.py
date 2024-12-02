import boto3
import json
import base64

def get_prompt():
    return input("Entre com a descrição para gerar imagem (em inglês): ")

def get_nome_arquivo():
    return input("Entre com nome do arquivo (exemplo: 'camisa.png'): ")

client = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")

prompt = get_prompt()
nome_arquivo = get_nome_arquivo()

titan_image_config = json.dumps({
    "textToImageParams": {
        "text": prompt
    },
    "taskType": "TEXT_IMAGE",
    "imageGenerationConfig": {
        "cfgScale": 10,
        "seed": 0,
        "quality": "standard",
        "width": 1024,
        "height": 1024,
        "numberOfImages": 1,
    }
})

response = client.invoke_model(
    body=titan_image_config,
    modelId="amazon.titan-image-generator-v1",
    accept="application/json",
    contentType="application/json")

response_body = json.loads(response.get("body").read())
base64_image = response_body.get("images")[0]
base_64_image = base64.b64decode(base64_image)

with open(nome_arquivo, "wb") as f:
    f.write(base_64_image)

print(f"Imagem salva como {nome_arquivo}")
