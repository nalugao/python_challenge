"""Permita ao usuário fazer uma lista de compras interativa:
Adicionar item (nome, quantidade)
Ver lista de compras
Marcar item como comprado
Remover item da lista
Sair"""

def ver_lista(dicionario_compras):
    print('-.-'*20)   
    if not dicionario_compras:
        print('A lista está vazia. Adicione itens pressionando a opção 2 no Menu.')
        print('-.-'*20)
        return
    
    print('Lista de compras:\n')
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
    nome_item = input('Nome do item: ').strip().title()
    qtd = int(input('Quantidade para item novo || Quantidade para somar em item já existente: ')) 
    
    if nome_item in dicionario_compras:
        print(f'\nEsse item já está na lista. A quantidade foi atualizada.')
        dicionario_compras[nome_item]['qtd'] += qtd
    else:
        dicionario_compras[nome_item] = {
            "qtd": qtd,
            "checked": False
        }
        print('\nItem inserido na lista de compras com sucesso!')
    print('-.-'*20)
    
def marcar_item(dicionario_compras):
    print('-.-'*20)
    nome_item = input('Nome do item que foi comprado: ').strip().title()
    if not nome_item in dicionario_compras:
        print('Erro: solicitação não concluída pois esse item não consta na lista de compras.')
        return # finaliza função e volta para o menu    
    print('\nEste item foi comprado!')
    print('-.-'*20)   
    
    dicionario_compras[nome_item]['checked'] = True

def remover_item(dicionario_compras):
    print('-.-'*20)
    nome_item = input('Nome do item que será removido: ').strip().title()
    if not nome_item in dicionario_compras:
        print('Erro: solicitação não concluída pois esse item não consta na lista de compras.')
        return
    print('\nItem removido da lista de compras com sucesso!')
    print('-.-'*20)
    
    dicionario_compras.pop(nome_item)

def main():
    dicionario_compras = {
        
    }
        
    print('\nBem vinda(o) a sua lista de compras!')

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
        opcao = input('Insira o número da opção desejada: ')
        
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