def restaurante():
    pedidos_pendentes = []
    pedidos_concluidos = []

    while True:
        print("\n Gerenciamento do Restaurante: ")
        print("1: Registrar Novo Pedido")
        print("2: Atualizar Status do Pedido")
        print("3: Remover Pedido Concluído")
        print("4: Visualizar Pedidos Pendentes e Concluídos")
        print("5: Sair do Sistema")

        try:
            menu = int(input("Digite o número do menu: "))

            if menu == 1:
                while True:
                    print("\n Menu de Pratos:")
                    print("1: Strogonoff")
                    print("2: Macarronada")
                    print("3: Churrasco")
                    print("4: Feijoada")
                    print("0: Voltar ao menu principal")
                    
                    pedido = int(input("Digite o pedido: "))
                    
                    if pedido == 0:
                        break
                    elif pedido in [1, 2, 3, 4]:                        
                        quantidade = int(input("Digite a quantidade desejada: "))
                        if pedido == 1:
                            prato = "Strogonoff"
                        elif pedido == 2:
                            prato = "Macarronada"
                        elif pedido == 3:
                            prato = "Churrasco"
                        elif pedido == 4:
                            prato = "Feijoada"
                        print(f"Pedido: Você pediu a quantidade de {quantidade} prato(s) de {prato}")
                        pedidos_pendentes.append({"prato": prato, "quantidade": quantidade})
                        print("Pedido registrado com sucesso!")
                    else:
                        print("Escolha um prato disponível")
            elif menu == 2:
                if pedidos_pendentes:
                    print("Pedidos Pendentes:")
                    for i, pedido in enumerate(pedidos_pendentes, 1):
                        print(f"{i}. {pedido['quantidade']} x {pedido['prato']}")
                    num_pedido = int(input("Digite o número do pedido para atualizar como concluído: "))
                    if 1 <= num_pedido <= len(pedidos_pendentes):
                        pedido_concluido = pedidos_pendentes.pop(num_pedido - 1)
                        pedidos_concluidos.append(pedido_concluido)
                        print("Status do pedido atualizado para concluído!")
                    else:
                        print("Número do pedido inválido.")
                else:
                    print("Não há pedidos pendentes para atualizar.")
            elif menu == 3:
                if pedidos_concluidos:
                    print("Pedidos Concluídos:")
                    for i, pedido in enumerate(pedidos_concluidos, 1):
                        print(f"{i}. {pedido['quantidade']} x {pedido['prato']}")
                    num_pedido = int(input("Digite o número do pedido para remover: "))
                    if 1 <= num_pedido <= len(pedidos_concluidos):
                        pedidos_concluidos.pop(num_pedido - 1)
                        print("Pedido removido com sucesso!")
                    else:
                        print("Número do pedido inválido.")
                else:
                    print("Não há pedidos concluídos para remover.")
            elif menu == 4:
                print("Pedidos Pendentes:")
                for i, pedido in enumerate(pedidos_pendentes, 1):
                    print(f"{i}. {pedido['quantidade']} x {pedido['prato']}")
                print("Pedidos Concluídos:")
                for i, pedido in enumerate(pedidos_concluidos, 1):
                    print(f"{i}. {pedido['quantidade']} x {pedido['prato']}")
            elif menu == 5:
                print("Encerrando gerenciador, Até Logo!")
                break
            else:
                print("Essa opção não existe no menu, tente novamente")
        except ValueError:
            print("Insira uma opção válida")

restaurante()
