import asyncio
from asyncio import sleep


async def robot(start: int = 0):
    while True:
        print(start)
        start += 1
        await sleep(1)


async def main():
    start = input()
    assert start.replace('-', '', 1).isdigit(), "The starting number must be an integer!"
    start = int(start)
    await robot(start)

asyncio.run(main())
