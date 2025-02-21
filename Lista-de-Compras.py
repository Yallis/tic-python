# Lista de Compras

def Lista_de_Compras():
    nome_produtos = []
    uniMed_produtos = []
    quantidade_produtos = []
    descricao_produtos = []

    lista_de_compras = []

    unidades_de_medida = ["kg", "g", "l", "ml", "un", "m", "cm"]

    def Mostrar_Lista(): # funcao para exibir os elementos da lista de compras
        i = 0
        for produto in nome_produtos:
            # exibe a lista de produtos no formato: "id". "nome do produto" - "quantidade" "unidade de medida" ("descrição do produto")
            print(i+1, ". " + produto, " - ", quantidade_produtos[i], uniMed_produtos[i], " (", descricao_produtos[i], ")")
            i += 1

    print()
    print("Bem vindo ao aplicativo Lista de Compras Simples.")
    print()

    while True:
        print()
        print("Lista de compras: ")

        if nome_produtos:
            print()
            Mostrar_Lista()

        print()
        print("A. Adicionar produto")
        print("B. Remover produto")
        print("C. Pesquisar produtos")
        print("D. Sair do programa")

        opcaoEscolhida = input("Selecione uma das opções acima: ")

        if opcaoEscolhida == 'D' or opcaoEscolhida == 'd':
            print()
            ipt_sair = input("Os itens da lista de compras não ficarão salvos. Tem certeza que deseja sair? y/n ")
            if ipt_sair == 'y' or ipt_sair == 'Y':
                print()
                print("Obrigado por utilizar a Lista de Compras. Volte sempre.")
                break
            else: continue


        if opcaoEscolhida not in ['A', 'B', 'C', 'a', 'b', 'c']:
            print()
            print("** Opção inválida! Tente novamente. **")
            continue

        # Adicionar produto a lista de compras
        if opcaoEscolhida == 'A' or opcaoEscolhida == 'a':
            print()
            ipt_nome = input("Informe o nome do produto que deseja adicionar à lista de compras: ")
            nome_produtos.append(ipt_nome)

            opcoes_Maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
            opcoes_minusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            lista_de_unidades = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]

            while True:
                print()
                print("Qual a unidade de medida do produto?")
                print()
                # Imprime a lista de opções de medidas de unidade
                for opcao in opcoes_Maiusculo:
                    print(opcao, ". ", lista_de_unidades[opcoes_Maiusculo.index(opcao)])

                ipt_unidade = input("Selecione uma opção: ")

                if ipt_unidade in opcoes_Maiusculo:
                    uniMed_produtos.append( unidades_de_medida[opcoes_Maiusculo.index(ipt_unidade)] )
                    break
                elif ipt_unidade in opcoes_minusculo:
                    uniMed_produtos.append( unidades_de_medida[opcoes_minusculo.index(ipt_unidade)] )
                    break
                else:
                    print("** Opção inválida! Tente novamente. **")
                    continue

            while True:
                print()
                try:
                    ipt_quantidade = float(input("Informe quantos(as) " + lista_de_unidades[ unidades_de_medida.index(uniMed_produtos[-1]) ] + "(s) de " + nome_produtos[-1] + " devem ser adicionados a lista: "))

                    if ipt_quantidade <= 0:
                        print()
                        print("** A quantidade não pode ser menor ou igual a zero. Tente novamente. **")
                        continue

                    quantidade_produtos.append(ipt_quantidade)
                    break
                except ValueError:
                    print()
                    print("** A quantidade deve ser um número maior que zero. Tente novamente. **")
                    continue

            print()
            ipt_descricao = input("Forneça uma descriçao sobre o produto: ")
            descricao_produtos.append(ipt_descricao)

            print()
            print("O seginte item foi adicionado a lista de compras: ")
            print(" . " + nome_produtos[-1], " - ", quantidade_produtos[-1], uniMed_produtos[-1], " (", descricao_produtos[-1], ")")
            print()
            input("Tecle 'Enter' para continuar.")


        # Remover produto da lista de compras
        if opcaoEscolhida == 'B' or opcaoEscolhida == 'b':
            if not nome_produtos: # verifia se a lista de produtos está vazia
                print()
                print("** A lista está vazia, adicione produtos a lista de compras antes de removê-los. **")
                continue
            else:
                print("")
                print("Remover produto da lista de compras: ")
                print()
                Mostrar_Lista()
                print()
                id_remover = float(input("Informe o ID equivalente do produto que deseja remover da lista de compras: "))
                nome_produtos.pop(int(id_remover-1))
                uniMed_produtos.pop(int(id_remover-1))
                quantidade_produtos.pop(int(id_remover-1))
                descricao_produtos.pop(int(id_remover-1))

                print()
                print("O item foi removido da lista de compras.")
                print()
                input("Tecle 'Enter' para continuar.")

        # Pesquisar por produto na lista de compras
        if opcaoEscolhida == 'C' or opcaoEscolhida == 'c':
            print()
            print("Pesquisar:")

            if not nome_produtos: # verifia se a lista de produtos está vazia
                print()
                print("** A lista está vazia, adicione produtos a lista de compras antes de fazer uma pesquisa. **")
                continue

            print()
            ipt_pesquisa = input("Informe o nome do produto que gostaria de pesquisar: ")

            print()
            _count = 0
            for produto in nome_produtos:
                if ipt_pesquisa in produto:
                    _count += 1
                    _index = nome_produtos.index(produto)
                    print(_index+1, ". " + nome_produtos[_index], " - ", quantidade_produtos[_index], uniMed_produtos[_index], " (", descricao_produtos[_index], ")")

            if _count > 0:
                print()
                if _count > 1:
                    print("Os", _count, " produtos acima foram encontrados como equivalentes a sua pesquisa.")
                else:
                    print("O produto acima foi encontrado como equivalente a sua pesquisa.")
            else:
                print("Não foram encontrados produtos na lista de compras correspondentes a sua pesquisa.")

            print()
            input("Tecle 'Enter' para continuar.")

Lista_de_Compras()