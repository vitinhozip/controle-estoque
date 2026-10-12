def mostrar_menu():
    print('---CONTROLE DE ESTOQUE AUTOMOTIVO---')
    print('1. Adicionar Produto')
    print('2. Remover Produto')
    print('3. Ver estoque')
    print('4. Sair')


def ler_inteiro(mensagem):
    while True:
        try:
            numero = input(mensagem)
            numero_int = int(numero)

            return numero_int
        except ValueError:
            print('Erro, digite novamente')


def adicionar_produto(estoque):
    produto = input('Digite o nome do produto que deseja adicionar: ').strip()
    if produto == '':
        print('Digite o nome do produto.')
        return

    quantidade_int = ler_inteiro('Digite a quantidade: ')

    if quantidade_int <= 0:
        print('Erro: A quantidade deve ser maior que 0.')
        return

    existe = False
    for item in estoque:
        if item['nome'].lower() == produto.lower():
            item['quantidade'] += quantidade_int
            existe = True
            break
    if not existe:
        estoque.append({'nome': produto, 'quantidade': quantidade_int})
    print(f'{quantidade_int}x {produto} adicionado(s) com sucesso!')



def remover_produto(estoque):
    if len(estoque) <= 0:
        print('Estoque vazio')
        return
    
    if len(estoque) > 1:
        ver_estoque(estoque)
        indice_int = (ler_inteiro('Digite o índice que deseja remover: '))
        if not 0 <= indice_int < len(estoque):
            print('Erro: índice não existe na lista.')
            return

    else:
        indice_int = 0
        print(f'Como só há um produto cadastrado no estoque, o produto {estoque[0]["nome"]} foi selecionado automaticamente')
    item_atual = estoque[indice_int]

    if item_atual['quantidade'] > 1:
        qnt_int = ler_inteiro(f'O item {item_atual["nome"]} tem {item_atual["quantidade"]} unidades. Quantas deseja remover? ')
        if qnt_int <= 0:
            print('Erro: A quantidade a remover deve ser maior que zero.')
        elif qnt_int == item_atual['quantidade']:
            item_removido = estoque.pop(indice_int)
            print(f'O item {item_removido["nome"]} foi removido do seu estoque!')
        elif qnt_int > item_atual['quantidade']:
            print(f'Erro: existem apenas {item_atual["quantidade"]} unidade(s) de {item_atual["nome"]}')
        else:
            estoque[indice_int]['quantidade'] -= qnt_int
            print(f'{qnt_int} unidade(s) de {item_atual["nome"]} removida(s). Restam {item_atual["quantidade"]}')
    else:
        item_removido = estoque.pop(indice_int)
        print(f'O item {item_removido["nome"]} foi removido do seu estoque!')



def ver_estoque(estoque):
    if estoque:
        for i, produto in enumerate(estoque):
            print(f'{i}: {produto["nome"]}: {produto["quantidade"]} unidade(s)')
    else:
        print('Estoque vazio.')


def main():
    estoque = []
    while True:
        mostrar_menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            adicionar_produto(estoque)

        elif opcao == '2':
            remover_produto(estoque)

        elif opcao == '3':
            ver_estoque(estoque)

        elif opcao == '4':
            print('Saindo do sistema...')
            break

        else:
            print('Escolha uma opção válida')


main()
