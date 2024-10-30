import asyncio
from time import sleep

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i+1} шар' )
    print(f'Силач {name} закончил соревнования.')
async def sorevnovanie():
    first=asyncio.create_task(start_strongman('Pasha', 3))
    second=asyncio.create_task(start_strongman('Denis', 4))
    third=asyncio.create_task(start_strongman('Apollon', 5))
    await first
    await second
    await third
asyncio.run(sorevnovanie())
