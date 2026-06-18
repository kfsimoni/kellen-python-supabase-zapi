import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_INSTANCE_TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


def validar_configuracoes():
    variaveis = {
        "SUPABASE_URL": SUPABASE_URL,
        "SUPABASE_KEY": SUPABASE_KEY,
        "ZAPI_INSTANCE_ID": ZAPI_INSTANCE_ID,
        "ZAPI_INSTANCE_TOKEN": ZAPI_INSTANCE_TOKEN,
        "ZAPI_CLIENT_TOKEN": ZAPI_CLIENT_TOKEN,
    }

    faltando = [
        nome
        for nome, valor in variaveis.items()
        if not valor
    ]

    if faltando:
        raise EnvironmentError(
            f"Variáveis não configuradas: {', '.join(faltando)}"
        )