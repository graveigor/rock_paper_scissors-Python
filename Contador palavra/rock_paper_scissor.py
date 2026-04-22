import os
os.system('cls' if os.name == 'nt' else 'clear')

# --- Rock, paper and scissor game --- (Python)

import random 
def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"] 
    escolha_computador = random.choice(opcoes) 
    escolha_usuario = input("Escolha: pedra, papel ou tesoura? ").lower() 

    if escolha_usuario not in opcoes: 
        print("Escolha inválida!") 
        return 

    print(f"Computador escolheu: {escolha_computador}") 