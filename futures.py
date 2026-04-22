import os
os.system('cls' if os.name == 'nt' else 'clear')

# Objeto que representa um valor indefinido que pode ser definido no futuro, geralmente usado em integração com APIs de baixo nível.

import asyncio

async def corrotina(futuro):
    print("Início!")
    await asyncio.sleep(2)
    futuro.set_result("Fim!")

async def main () :
    # asyncio.future -> utilizado para criar um futuro
    futuro = asyncio.Future ()
    asyncio. create_task (corrotina (futuro))
    resultado = await futuro
    print(resultado)

asyncio.run(main())

# Saída : Início!
# Fim!