print("===" * 20)
print("Olá! Seja bem-vindo(a) ao Supermercado Atacabolso ")
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
    ["Feijão",10,99],
    ["Arroz",8,60],
    ["Peito de Frango",19,90],
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

carrinho = [] #carrinho vazio para adicionar os produtos
total = 0 #valor total da compra a pagar

while True:
    print("\nProdutos disponíveis:")
    for i, produto in enumerate(produtos):
        print(f"{i + 1}. {produto[0]:<15} - R${produto[1]:.2f}")

    print("\nOpções:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Finalizar compra")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        while True:
            try:
                indice = int(input("Digite o número do produto: ")) - 1
                if 0 <= indice < len(produtos):
                    quantidade = int(input(f"Digite a quantidade de {produtos[indice][0]}: "))
                    if quantidade > 0:
                        # Adiciona o produto ao carrinho com a quantidade
                        carrinho.append([produtos[indice][0], produtos[indice][1], quantidade])
                        total = total + produtos[indice][1] * quantidade
                        print(f"{quantidade}x {produtos[indice][0]} adicionados ao carrinho.")
                        break
                    else:
                        print("A quantidade deve ser maior que zero.")
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")

    elif opcao == '2':
        if len(carrinho) == 0:
            print("O carrinho está vazio.")
        else:
            print("\nItens no carrinho:")
            for i, item in enumerate(carrinho):
                print(f"{i + 1}. {item[2]}x {item[0]:<30} - R${item[1]:.2f} (Total: R${item[1] * item[2]:.2f})")
            while True:
                try:
                    indice = int(input("Digite o número do produto a ser removido: ")) - 1
                    if 0 <= indice < len(carrinho):
                        produto_removido = carrinho.pop(indice)
                        total -= produto_removido[1] * produto_removido[2]
                        print(f"{produto_removido[2]}x {produto_removido[0]} removidos(as) do carrinho.")
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")

    elif opcao == '3':
        print("\nItens no carrinho:")
        for item in carrinho:
            print(f"{item[2]}x {item[0]:<15} - R${item[1]:.2f} (Total: R${item[1] * item[2]:.2f})")
        print(f"\nValor total: R${total:.2f}")

        try:
            pagamento = float(input("Digite o valor para pagamento: R$"))
            troco = pagamento - total
            if troco >= 0:
                print(f"Troco: R${troco:.2f}")
                print("Obrigado pela sua compra! Volte sempre!")
            else:
                print("Valor pago insuficiente.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico.")

    else:
        print("Opção inválida.")

    if opcao == '4':
        # Sair
        print("Saindo do sistema. Até logo!")
        break