import afl
import sys

afl.init()


def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k - num_lessoreq)
    else:
        return pivot


def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        steps.append((start, end))
        steps.extend(hanoi(height - 1, helper, end))

    return steps


input_lines = sys.stdin.readlines()
input_lines = [line.strip() for line in input_lines]
if len(input_lines) == 1:
    height = int(input_lines[0])
    hanoi(height, start=1, end=3)
else:
    arr = input_lines[0].strip()
    arr = list(map(int, arr.split()))
    k = int(input_lines[1])
    kth(arr, k)
