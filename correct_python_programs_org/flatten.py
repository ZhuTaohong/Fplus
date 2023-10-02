import afl
import sys

afl.init()

def flatten(arr):
    for x in arr:
        if isinstance(x, list):
            for y in flatten(x):
                yield y
        else:
            yield x

input_lines = sys.stdin.readlines()
input_lines = [line.strip() for line in input_lines]
arr = input_lines[0].strip()
arr = list(map(int, arr.split()))

flatten(arr)