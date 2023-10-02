import afl
import sys

afl.init()

def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    while lo < hi:
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1

input_lines = sys.stdin.readlines()
input_lines = [line.strip() for line in input_lines]
arr = input_lines[0].strip()
arr = list(map(int, arr.split()))
x = int(input_lines[1])
find_first_in_sorted(arr, x)



