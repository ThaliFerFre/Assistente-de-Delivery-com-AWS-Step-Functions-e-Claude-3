# assistant.py

def gerar_sugestoes(pedido):
    # Sugestões fictícias baseadas no pedido
    sugestoes = {
        "macarrão": ["Vinho Tinto", "Molho Alfredo", "Queijo Parmesão"],
        "pizza": ["Refrigerante", "Cerveja", "Molho de Pimenta"],
        "sushi": ["Saquê", "Chá Verde", "Molho de Soja"]
    }
    return sugestoes.get(pedido.lower(), ["Sem sugestões disponíveis"])

def main():
    pedido = input("Qual é o seu pedido? ")
    sugestoes = gerar_sugestoes(pedido)
    print("Sugestões para complementar seu pedido:")
    for sugestao in sugestoes:
        print(f"- {sugestao}")

if __name__ == "__main__":
    main()
