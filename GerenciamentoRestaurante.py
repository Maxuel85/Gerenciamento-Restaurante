def restaurante():
    while True:
        print("\nGerenciamento do Restaurante: ")
        print("1: Visualizar Produtos em Estoque")
        print("2: Substituir Produtos")
        print("3: Adicionar Novos Produtos")
        print("4: Remover Produtos")
        print("5: Consultar Detalhes de um Produto")
        print("6: Sair do Sistema")

        try:
            menu = int(input("Digite o número do menu: "))

            if menu == 6:
                print("Encerrando gerenciador, Até Logo!")
                break
            else:
                print("Essa opção não existe no menu, tente novamente")
        except ValueError:
            print("Insira uma opção válida")

restaurante()
    