import random

def numero_aleatorio():
    return random.randint(2, 100)

def tentativa_do_usuario():
  
    print('Esse é o jogo "Acerte o número aleatório"')

    aleatorio = numero_aleatorio()

    numero = int(input("Digite o primeiro número do tipo inteiro: "))
    contador = 1
    
    while numero != aleatorio:
        if  numero <= aleatorio - 10:
            print("O número escolhido está muito abaixo do número aleatório. Tente novamente.")
        
        elif numero <= aleatorio - 5:
            print("O número escolhido está próximo do número aleatório mas ainda está abaixo. Tente novamente.")
        
        elif numero < aleatorio:
            print("O número escolhido está muito próximo do número aleatório mas ainda está abaixo. Tente novamente.")
        
        elif  numero >= aleatorio + 10:
            print("O número escolhido está muito acima do número aleatório. Tente novamente.")
                      
        elif numero >= aleatorio + 5:
            print("O número escolhido está próximo do número aleatório mas ainda está acima. Tente novamente.")
            
        elif numero > aleatorio:
            print("O número escolhido está muito próximo do número aleatório mas ainda está acima. Tente novamente.")

        numero = int(input("Digite um número do tipo inteiro: ")) 
        contador += 1
        
    print(f'Parabéns! Você acertou o número aleatório em {contador} tentativas!')
               
tentativa_do_usuario()
