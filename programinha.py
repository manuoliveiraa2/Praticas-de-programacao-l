print("===" * 20)
print("Olá! Seja bem-vindo(a) ao Hortifruti Five's ")
print("===" * 20)


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
    
]

carrinho = [] #carrinho vazio para adicionar os produtos
total = 0 #valor total da compra a pagar

while True:
    print("\nProdutos disponíveis:")
    for i, produto in enumerate(produtos):
        print(f"{i+1}. {produto[0]:<10} - R${produto[1]:.2f}")

    print("\nOpções:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Finalizar compra")

    opcao = input("Digite a opção desejada:")

    if opcao == '1':
        while True:
        
                indice = int(input("Digite o número do produto:")) - 1
                if 0 <= indice < len(produtos):
                    carrinho.append(produtos[indice])
                    total = total + produtos[indice][1]
                    print(f"{produtos[indice][0]} adicionado ao carrinho.")
                    break

                else:
                    print("Opção inválida.")
                    
    elif opcao == '2':
        if len(carrinho) == 0:
            print("O carrinho está vazio.")
        else:
            for i, item in enumerate(carrinho):
                print(f"{i+1} {item[0]}")
            while True:

                    indice = int(input("Digite o número do produto a ser removido:")) - 1
                    if 0 <= indice < len(carrinho):
                        produto_removido = carrinho.pop(indice)
                        total = total - produto_removido[1]
                        print(f"{produto_removido[0]} removido do carrinho.")
                        break
                    else:
                        print("Opção inválida.")

    elif opcao == '3':
        print("\nItens no carrinho:")
        for item in carrinho:
            print(f"{item[0]:<10} - R${item[1]:.2f}")
        print(f"\nValor total: R${total:.2f}")

        pagamento = float(input("Digite o valor para pagamento:"))
        troco = pagamento - total
        if troco >= 0:
            print(f"Troco: R${troco:.2f}")
        else:
            print("Valor pago insuficiente.")
        break
    else:
        print("Opção inválida.")