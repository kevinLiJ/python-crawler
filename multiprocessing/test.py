import multiprocessing
import time


def worker():
    n = 20
    while n > 0:
        print(n)
        n -= 1


if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p1 = multiprocessing.Process(target=worker)
    p.start()
    p1.start()
