def restaurante():
    while True:
        print("\nGerenciamento do Restaurante: ")
        print("1: Registrar Novo Pedido")
        print("2: Atualizar Status do Pedido")
        print("3: Remover Pedido Concluído")
        print("4: Visualizar Pedidos Pendentes e Concluídos")
        print("5: Sair do Sistema")

        try:
            menu = int(input("Digite o número do menu: "))

            if menu == 5:
                print("Encerrando gerenciador, Até Logo!")
                break
            else:
                print("Essa opção não existe no menu, tente novamente")
        except ValueError:
            print("Insira uma opção válida")

restaurante()
    