import afl
import sys

afl.init()

def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):
        sorted_arr.extend([i] * count)

    return sorted_arr

input_lines = sys.stdin.readlines()
input_lines = [line.strip() for line in input_lines]
arr = input_lines[0].strip()
arr = list(map(int, arr.split()))
k = int(input_lines[1])
bucketsort(arr, k)
