import argparse

from asyncio import sleep, run

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, default=0, help='Start number')

args = parser.parse_args()


async def robot(start: int = 0):
    while True:
        print(start)
        start += 1
        await sleep(1)


run(robot(args.start))
