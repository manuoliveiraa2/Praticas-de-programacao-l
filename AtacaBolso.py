def tela_inicial():
    print("===" * 20)
    print("Bem-vindo(a) ao Supermercado Atacabolso! v.0001")
    print("===" * 20)
    print("\n1. Iniciar compra")
    print("2. Sair")
    return input("\nDigite a opção desejada: ")

# Função para exibir os produtos disponíveis
def exibir_produtos(produtos):
    print("\nProdutos disponíveis:")
    for i, produto in enumerate(produtos):
        print(f"{i + 1}. {produto[0]:<20} - R${produto[1]:.2f}")

# Função para exibir os itens no carrinho
def exibir_carrinho(carrinho):
    if len(carrinho) == 0:
        print("\nO carrinho está vazio.")
    else:
        print("\nItens no carrinho:")
        for i, item in enumerate(carrinho):
            print(f"{i + 1}. {item[2]}x {item[0]:<15} - R${item[1]:.2f} (Total: R${item[1] * item[2]:.2f})")

# Função para adicionar produtos ao carrinho
def adicionar_produtos(produtos, carrinho):
    try:
        entrada = input("Digite os produtos e quantidades no formato ID-quantidade (ex.: 1-2, 3-1): ")
        itens = [item.strip() for item in entrada.split(",")]
        total_adicionado = 0
        for item in itens:
            try:
                produto_id, quantidade = map(int, item.split("-"))
                produto_id -= 1  # Ajustar para índice da lista
                if 0 <= produto_id < len(produtos) and quantidade > 0:
                    # Verificar se o produto já está no carrinho
                    produto_encontrado = False
                    for produto in carrinho:
                        if produto[0] == produtos[produto_id][0]:
                            produto[2] += quantidade
                            produto_encontrado = True
                            break
                    if not produto_encontrado:
                        carrinho.append([produtos[produto_id][0], produtos[produto_id][1], quantidade])
                    total_adicionado += produtos[produto_id][1] * quantidade
                    print(f"{quantidade}x {produtos[produto_id][0]} adicionados ao carrinho.")
                else:
                    print(f"ID {produto_id + 1} ou quantidade inválida.")
            except ValueError:
                print(f"Formato inválido para '{item}'. Use ID-quantidade.")
        return total_adicionado
    except ValueError:
        print("Erro na entrada. Por favor, insira no formato correto.")
        return 0

# Função para remover produto do carrinho
def remover_produto(carrinho):
    if len(carrinho) == 0:
        print("\nO carrinho está vazio.")
        return 0
    else:
        exibir_carrinho(carrinho)
        while True:
            try:
                indice = int(input("Digite o número do produto a ser removido: ")) - 1
                if 0 <= indice < len(carrinho):
                    produto_removido = carrinho.pop(indice)
                    print(f"{produto_removido[2]}x {produto_removido[0]} removidos do carrinho.")
                    return produto_removido[1] * produto_removido[2]
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")

# Lista de produtos disponíveis
produtos = [
    ["Maçã", 2.50],
    ["Banana", 1.99],
    ["Laranja", 3.20],
    ["Melancia", 6.00],
    ["Morango", 10.80],
    ["Pitaya", 17.00],
    ["Abacaxi", 3.50],
    ["Goiaba", 5.00],
    ["Melão", 7.10],
    ["Feijão",10.99],
    ["Arroz",8.60],
    ["Peito de Frango",19.90],
    ["Cerveja heineken" ,6.79],
    ["Cerveja corona" ,6.59],
    ["Lã de aço bom" ,2.85],
    ["Biscoito oreo" ,3.75],
    ["Bis xtra" ,3.49],
    ["Detergente"  ,2.35],
    ["Pizza" ,16.68],
    ["Sanduiche" ,7.48],
    ["Leite Ninho em pó", 22.49],
    ["Refrigerante Coca Cola", 15.00],
    ["Biscoito Maria", 6.29],
    ["Achocolatado", 6.90],
    ["Papel Higiênico", 15.90],
    ["Macarrão", 4.50],
    ["Molho de tomate", 3.50],
    ["Pão de Queijo", 21.50],
    ["Linguiça de Frango", 16.50],
    ["Salame Italiano", 28.80],
    ["Queijo Mussarela",10.44],
    ["30 Ovos", 20.00]
]

# Loop principal do programa
while True:
    opcao_inicial = tela_inicial()

    if opcao_inicial == '1':  # Iniciar compra
        carrinho = []  # Carrinho vazio para adicionar os produtos
        total = 0  # Valor total da compra a pagar

        while True:
            exibir_produtos(produtos)
            print("\nOpções:")
            print("1. Adicionar produtos (vários de uma vez)")
            print("2. Remover produto")
            print("3. Finalizar compra")
            print("4. Cancelar compra e voltar ao menu inicial")

            opcao = input("\nDigite a opção desejada: ")

            if opcao == '1':  # Adicionar produtos
                total += adicionar_produtos(produtos, carrinho)

            elif opcao == '2':  # Remover produto
                total -= remover_produto(carrinho)

            elif opcao == '3':  # Finalizar compra
                exibir_carrinho(carrinho)
                print(f"\nValor total: R${total:.2f}")
                try:
                    pagamento = float(input("Digite o valor para pagamento: R$"))
                    troco = pagamento - total
                    if troco >= 0:
                        print(f"Troco: R${troco:.2f}")
                        print("Obrigado pela sua compra! Volte sempre!")
                        break
                    else:
                        print("Valor pago insuficiente.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um valor numérico.")
                break

            elif opcao == '4':  # Cancelar compra
                print("Compra cancelada. Retornando ao menu inicial...")
                break

            else:
                print("Opção inválida.")

    elif opcao_inicial == '2':  # Sair do programa
        print("Obrigado por visitar o Supermercado Atacabolso! Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")