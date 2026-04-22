import os
os.system('cls' if os.name == 'nt' else 'clear')

# Corrotina é uma função especial que pode ser 'pausada' e retomada durante a sua execução. É uma função que permite que o código aguarde algo acontecer sem bloquear todo o programa.
import asyncio
async def corrotina():
    print("Início")
    await asyncio.sleep(2)
    print("Fim!")
    
# Usamos o run ou await para executa-la, pois é o único modo de executa-la, identifica como assíncrona
asyncio.run(corrotina())

# --- Exemplo com await ---

import asyncio
async def corrotina2(numero):
    print(f"Iniciando a tarefa {numero}")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")
    
async def main():
    await corrotina2 (1)
    await corrotina2 (2)
    
asyncio.run(main())

# Saída: Iniciando tarefa 1
# Tarefa 1 concluída!
# Iniciando tarefa 2
# Tarefa 2 concluída!