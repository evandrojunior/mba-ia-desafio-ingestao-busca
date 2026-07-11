from search import search_prompt

def main():
    question = input("Faça sua pergunta:\n\nPERGUNTA: ")
    chain = search_prompt(question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print(f"RESPOSTA: {chain}")

if __name__ == "__main__":
    main()