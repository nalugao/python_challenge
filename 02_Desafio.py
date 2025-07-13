#Peça duas strings e diga se elas são iguais ou diferentes ou se uma esta contida na outra

def comparar_strings():
    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")

    if string1 == string2:
        print("As strings são iguais.")
    elif string1 in string2:
        print(f"A primeira string '{string1}' está contida na segunda string '{string2}'.")
    elif string2 in string1:
        print(f"A segunda string '{string2}' está contida na primeira string '{string1}'.")
    else:
        print("As strings são diferentes.")

comparar_strings()