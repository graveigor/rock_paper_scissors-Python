import os
os.system('cls' if os.name == 'nt' else 'clear')


# Tasks -> Executa uma corrotina de forma concorrente, permitindo que múltiplas corrotinas rodem juntas
import asyncio

async def corrotina(numero):
    print(f"Iniciando tarefa {numero}")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")
    
async def main():
    tarefa1 = asyncio.create_task(corrotina(1))
    tarefa2 = asyncio.create_task(corrotina(2))
    await tarefa1
    await tarefa2
    
asyncio.run(main())

# Saída : Iniciando tarefa 1
# Iniciando tarefa 2
# Tarefa 1 concluída!
# Tarefa 2 concluída!



# --- Tasks múltiplas ---

import asyncio

async def corrotina(nome, tempo):
    print(f"Tarefa {nome} iniciada")
    await asyncio.sleep(tempo)
    print(f"Tarefa {nome} concluída")
    
async def main2():
# .gather -> une e executa múltiplas corrotinas simuultaneamente
    await asyncio.gather(
        corrotina("1", 2),
        corrotina("2", 3),
        corrotina("3", 1)
    )

asyncio.run(main2())
