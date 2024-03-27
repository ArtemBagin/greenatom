import time


def robot(start: int = 0):
    while True:
        print(start)
        start += 1
        time.sleep(1)


def main():
    start = input()
    assert start.replace('-', '', 1).isdigit(), "The starting number must be an integer!"
    start = int(start)
    robot(start)
