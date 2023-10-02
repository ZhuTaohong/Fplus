import afl
import sys

afl.init()
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid + 1, end)
        else:
            return mid

    return binsearch(0, len(arr))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

input_lines = sys.stdin.readlines()
input_lines = [line.strip() for line in input_lines]
if len(input_lines) == 1:
    arr = input_lines[0].strip()
    arr = list(map(int, arr.split()))
    a = arr[0]
    b = arr[1]
    gcd(a, b)
else:
    arr = input_lines[0].strip()
    arr = list(map(int, arr.split()))
    x = int(input_lines[1])
    find_in_sorted(arr, x)
