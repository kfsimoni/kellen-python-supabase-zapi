import logging

from src.config import validar_configuracoes
from src.supabase_client import buscar_contatos_ativos
from src.zapi_client import enviar_mensagem_whatsapp


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    validar_configuracoes()

    contatos = buscar_contatos_ativos()

    if not contatos:
        logging.warning("Nenhum contato encontrado.")
        return

    logging.info(
        "%s contatos encontrados.",
        len(contatos)
    )

    for contato in contatos:
        nome = contato["nome"]
        telefone = contato["telefone"]

        logging.info(
            "Enviando mensagem para %s (%s)",
            nome,
            telefone
        )

        try:
            enviar_mensagem_whatsapp(
                nome,
                telefone
            )

            logging.info(
                "Mensagem enviada com sucesso."
            )

        except Exception as erro:
            logging.error(
                "Erro ao enviar para %s: %s",
                nome,
                erro
            )


if __name__ == "__main__":
    main()