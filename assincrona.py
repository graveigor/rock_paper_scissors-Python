import os
os.system('cls' if os.name == 'nt' else 'clear')

# Programação assíncrona
import time

def tarefa (numero):
    print(f"Iniciando tarefa {numero}.")
    time.sleep(2)
    print(f"Tarefa {numero} concluída!")
    
tarefa(1)
tarefa(2)
tarefa(3)
