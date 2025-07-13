"""DESAFIO 1

Peça o tempo (em minutos) para correr 5 km e classifique:

A: até 25 min → Atleta

B: 26 a 35 min → Bom condicionamento

C: 36 a 50 min → Regular

D: Acima de 50 min → A melhorar"""

def classificacao(tempo):
    tempo = int(input("Digite o tempo (em minutos) para correr 5 km: "))
    if tempo <= 25:
        print("Sua classificação é: Atleta")
    elif 26 <= tempo <= 35:
        print("Sua classificação é: Bom condicionamento")
    elif 36 <= tempo <= 50:
        print("Sua classificação é: Regular")
    else:
        print("Sua classificação é: A melhorar")

classificacao(tempo=0)