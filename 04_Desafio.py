"""Permita ao usuário fazer uma lista de compras interativa:
Adicionar item (nome, quantidade)
Ver lista de compras
Marcar item como comprado
Remover item da lista
Sair"""

def ver_lista(dicionario_compras: dict):
    print('-.-'*20)   
    if not dicionario_compras:
        print('A lista está vazia. Adicione itens pressionando a opção 2 no Menu.')
        print('-.-'*20)
        return
    
    print('Lista de compras:')
    for nome_item, item_detalhes in dicionario_compras.items():
        checked = item_detalhes["checked"]
        quantidade = item_detalhes["qtd"]
        if checked:
            print('[x]', nome_item, quantidade)
        else:
            print('[ ]', nome_item, quantidade)
    print('-.-'*20)
        
def adicionar_item(dicionario_compras):
    print('-.-'*20)
    nome_item = input('Nome do item: ')
    print('-.-'*20)
    qtd = int(input('Quantidade: '))
    print('-.-'*20)
    print('Item inserido na lista de compras com sucesso!')
    print('-.-'*20)
    
    dicionario_compras[nome_item] = {
        "qtd": qtd,
        "checked": False
    }
    
def marcar_item(dicionario_compras):
    print('-.-'*20)
    nome_item = input('Nome do item que foi comprado: ')
    if not nome_item in dicionario_compras:
        print('Erro: solicitação não concluída pois esse item não consta na lista de compras.')
        return # finaliza função e volta para o menu    
    print('-.-'*20)
    print('Este item foi comprado!')
    print('-.-'*20)   
    
    dicionario_compras[nome_item]['checked'] = True

def remover_item(dicionario_compras):
    print('-.-'*20)
    nome_item = input('Nome do item que será removido: ')
    if not nome_item in dicionario_compras:
        print('Erro: solicitação não concluída pois esse item não consta na lista de compras.')
        return
    print('-.-'*20)
    print('Item removido da lista de compras com sucesso!')
    print('-.-'*20)
    
    dicionario_compras.pop(nome_item)

def main():
    dicionario_compras = {
        
    }
        
    print('Bem vinda(o) a sua lista de compras!')

    while True:
        print('='*50)
        print('‖'+' '*22+'MENU'+' '*22+'‖')
        print('='*50)
        print('‖'+' '+'1. Ver lista'+' '*35+'‖')
        print('‖'+' '+'2. Adicionar item'+' '*30+'‖')
        print('‖'+' '+'3. Marcar como comprado'+' '*24+'‖')
        print('‖'+' '+'4. Remover item'+' '*32+'‖')
        print('‖'+' '+'5. Sair'+' '*40+'‖')
        print('='*50)
        opcao = input('Escolha uma opção: ')
        
        if opcao == "1" : 
            ver_lista(dicionario_compras)
        if opcao == "2" : 
            adicionar_item(dicionario_compras)
        if opcao == "3" : 
            marcar_item(dicionario_compras)
        if opcao == "4" : 
            remover_item(dicionario_compras)
        if opcao == "5" : 
            break
          
main()
