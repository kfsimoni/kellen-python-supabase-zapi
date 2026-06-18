import requests

from src.config import (
    ZAPI_INSTANCE_ID,
    ZAPI_INSTANCE_TOKEN,
    ZAPI_CLIENT_TOKEN,
)


def enviar_mensagem_whatsapp(nome, telefone):
    url = (
        f"https://api.z-api.io/instances/"
        f"{ZAPI_INSTANCE_ID}/token/"
        f"{ZAPI_INSTANCE_TOKEN}/send-text"
    )

    mensagem = f"Olá, {nome} tudo bem com você?"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    headers = {
        "Client-Token": ZAPI_CLIENT_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=15
    )

    print(f"\nStatus: {response.status_code}")
    print(f"Resposta: {response.text}")

    response.raise_for_status()

    return response.json()