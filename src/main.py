from src.supabase_client import buscar_contatos_ativos


def main():
    contatos = buscar_contatos_ativos()

    print("\nContatos encontrados:\n")

    for contato in contatos:
        print(contato)


if __name__ == "__main__":
    main()