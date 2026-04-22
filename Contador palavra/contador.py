import os
os.system('cls' if os.name == 'nt' else 'clear')

frase = input("Digite uma frase: ")
palavras = frase.split()
print(len(palavras))
print(palavras)


# -- Aprimorando código ---
def contar_palavras(frase):
    palavras = frase.split
    print(palavras)
    return len(palavras)