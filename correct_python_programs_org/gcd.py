import afl
import sys

afl.init()

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

input_lines = sys.stdin.readlines()
input_lines = [line.strip() for line in input_lines]
arr = input_lines[0].strip()
arr = list(map(int, arr.split()))
a = arr[0]
b = arr[1]

gcd(a, b)

