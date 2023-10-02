import afl
import sys

afl.init()


def bitcount(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


n = int(sys.stdin.readlines()[0])
bitcount(n)
