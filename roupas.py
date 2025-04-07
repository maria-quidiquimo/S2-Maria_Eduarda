def calcular_preco(produto):
    if produto == "camiseta":
        return 50
    elif produto == "Calça":
        return 100
    elif produto == "tênis":
        return 150
    elif produto == "jaqueta":
        return 200
    else:
        return -1  # Retorna -1 para indicar que o produto não foi encontrado

# Menu de opções para o cliente escolher
print("Bem vindo(a) à nossa loja de roupas!")
print("Escolha a roupa que deseja comprar")
print("1. Camiseta")
print("2. Calça")
print("3. Tênis")
print("4. Jaqueta")

# Solicitar ao cliente a escolha do produto
opcao = input("Digite o nome do produto que você deseja comprar: ").lower()

# Calcular o preço do produto
preco = calcular_preco(opcao)

# Verificar e exibir o preço ou mensagem de erro
if preco == -1:
    print("Desculpe, esse produto não está disponível em nossa loja.")
else:
    print(f"Você escolheu {opcao}. O preço é R${preco:.2f}.")
