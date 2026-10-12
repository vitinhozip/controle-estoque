# Estoque automotivo

Projeto de controle de estoque em Python que adiciona, remove e mostra o estado atual do estoque. Feito para praticar a implementação de funções em Python.

## Funcionalidades
- Adicionar itens ao estoque (se o produto já existe, a quantidade é somada)
- Remover itens total ou parcialmente
- Ver os itens que o estoque possui no momento

## Como executar
É necessário ter o Python 3 instalado. Execute o comando:

```
python estoque.py
```

## Exemplo de uso
```
---CONTROLE DE ESTOQUE AUTOMOTIVO---
1. Adicionar Produto
2. Remover Produto
3. Ver estoque
4. Sair
Escolha uma opção: 1
Digite o nome do produto que deseja adicionar: pneu
Digite a quantidade: 4
4x pneu adicionado(s) com sucesso!
```

## Estrutura do código

| Função | O que faz |
|---|---|
| `mostrar_menu` | Exibe o menu com as opções disponíveis. |
| `ler_inteiro` | Lê um número inteiro e repete a pergunta até receber um valor válido. É usada para ler a quantidade e o índice. |
| `adicionar_produto` | Pede o nome e a quantidade. Nome vazio ou quantidade menor ou igual a 0 geram erro e o usuário volta ao menu. Se o produto já existe (sem diferenciar maiúsculas de minúsculas), a quantidade é somada; caso contrário, o item é adicionado. |
| `remover_produto` | Remove um item total ou parcialmente. As regras estão na tabela abaixo. |
| `ver_estoque` | Mostra o índice, o nome e a quantidade de cada item, ou avisa que o estoque está vazio. |
| `main` | Cria a lista vazia `estoque` e mantém o laço `while` do menu, chamando a função da opção escolhida (1 adicionar, 2 remover, 3 ver o estoque, 4 sair). A opção 4 exibe uma mensagem e encerra o laço com `break`. Qualquer outra entrada pede uma opção válida. |

### Regras da remoção

| Situação | Resultado |
|---|---|
| Estoque vazio | O usuário é avisado e volta ao menu. |
| Mais de um item | O estoque é mostrado e o usuário informa o índice. Um índice inexistente gera erro. |
| Apenas um item | O item é selecionado automaticamente. |
| Item com 1 unidade | É removido direto, sem perguntar a quantidade. |
| Quantidade a remover menor ou igual a 0 | Mensagem de erro. |
| Quantidade menor que a existente | A quantidade é subtraída e o programa mostra quantas unidades restam. |
| Quantidade igual à existente | O item é totalmente removido. |
| Quantidade maior que a existente | Erro informando quantas unidades o produto possui, e o usuário volta ao menu. |

## Conceitos praticados
- Funções com parâmetros e `return`
- Estruturas condicionais e laços de repetição
- Listas de dicionários
- Manipulação de strings e de listas
- `try` e `except`
- Validação de entradas
