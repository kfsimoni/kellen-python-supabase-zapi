from supabase import create_client
from src.config import SUPABASE_URL, SUPABASE_KEY


def criar_cliente():
    return create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )


def buscar_contatos_ativos():
    supabase = criar_cliente()

    resposta = (
        supabase
        .table("contatos")
        .select("*")
        .eq("ativo", True)
        .limit(3)
        .execute()
    )

    return resposta.data