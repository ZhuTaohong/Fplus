import afl
import sys

afl.init()


def get_factors(n):
    if n == 1:
        return []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)

    return [n]


def kheapsort(arr, k):
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    for x in arr[k:]:
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)


input_lines = sys.stdin.readlines()
input_lines = [line.strip() for line in input_lines]
if len(input_lines) == 1:
    n = int(input_lines[0])
    get_factors(n)
else:
    arr = input_lines[0].strip()
    arr = list(map(int, arr.split()))
    k = int(input_lines[1])
    kheapsort(arr, k)
