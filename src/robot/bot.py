import argparse

from asyncio import sleep, run

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, help='Start number')

args = parser.parse_args()


async def robot(start: int = 0):
    while True:
        print(start)
        start += 1
        await sleep(1)


if args.start is None:
    start = input('Введите стартовое число: ')
    assert start.replace('-', '', 1).isdigit(), 'Start number must been integer'
    start = int(start)
else:
    start = args.start

run(robot(start))
