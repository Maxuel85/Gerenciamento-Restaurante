def restaurante():
    pedidos_pendentes = []
    pedidos_concluidos = []

    while True:
        print("\nGerenciamento do Restaurante: ")
        print("1: Registrar Novo Pedido")
        print("2: Atualizar Status do Pedido")
        print("3: Remover Pedido Concluído")
        print("4: Visualizar Pedidos Pendentes e Concluídos")
        print("5: Sair do Sistema")

        try:
            menu = int(input("Digite o número do menu: "))

            if menu == 1:
                pedido = input("Digite o pedido: ")
                pedidos_pendentes.append(pedido)
                print("Pedido registrado com sucesso!")
            elif menu == 2:
                if pedidos_pendentes:
                    print("Pedidos Pendentes:")
                    for i, pedido in enumerate(pedidos_pendentes, 1):
                        print(f"{i}. {pedido}")
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
                        print(f"{i}. {pedido}")
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
                    print(f"{i}. {pedido}")
                print("Pedidos Concluídos:")
                for i, pedido in enumerate(pedidos_concluidos, 1):
                    print(f"{i}. {pedido}")
            elif menu == 5:
                print("Encerrando gerenciador, Até Logo!")
                break
            else:
                print("Essa opção não existe no menu, tente novamente")
        except ValueError:
            print("Insira uma opção válida")

restaurante()