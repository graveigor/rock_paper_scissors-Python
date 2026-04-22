import os
os.system('cls' if os.name == 'nt' else 'clear')

# Extrai os elementos do índice 1 até o 2 (não inclui o índice 3), resultando em [20, 30].
lista = [10,20,30,40,]
print(lista[1:3])

## Extrai os elementos do índice 1 até o 2 (não inclui o índice 3), resultando em [20, 30].
tupla = (10,20,30,40,)
print(tupla[1:3])

# Operador in

lista = [10,20,30]
print(20 in lista)
print(40 in lista)

tupla = (10,20,30)
print(20 in tupla)
print(40 in tupla)

