"""Peça ao usuário o salário e o tempo de casa (em anos). Se o funcionário tiver mais de 5 anos, recebe 10% de bônus; senão, recebe 5%.
Mostre o valor do bônus e o novo salário."""

def ajuste_salario():
    aumento1 = 0.05
    aumento2 = 0.1
    
    salario_input = input('Informe seu salário, utilizando apenas números (ex: 1000.50 ou 1,000.50): ')
    salario = float(salario_input.replace(',', ''))
    
    try:
        
        tempo_trabalho = int(input('Informe seu tempo de trabalho na empresa em anos: '))
        
        if tempo_trabalho >= 5:
            bonus = salario*aumento2
            novo_salario = salario + bonus
        else:
            bonus = salario*aumento1
            novo_salario = salario + bonus

        print(f'Seu bonus é de R${bonus:.2f} e seu salario ajustado ficará R${novo_salario:.2f}')

    except ValueError:
        msg_error = "Erro: o valor está inserido de forma incorreta. Insira números inteiros."        
        print('='*len(msg_error))
        print(msg_error)
        print('='*len(msg_error))

    return

ajuste_salario()

      