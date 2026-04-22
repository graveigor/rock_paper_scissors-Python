import os
os.system('cls' if os.name == 'nt' else 'clear')


def somar(a, b):
    return a + b

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = somar(numero1,numero2)
print(f"A soma é: {resultado}")

# --- Tratar possíveis erros ---

def somar2(a, b):
    return a + b

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    resultado = somar2(numero1, numero2)
    print(f"A soma é: {resultado}")

except ValueError:
    print("Erro: Digite apenas números válidos!")