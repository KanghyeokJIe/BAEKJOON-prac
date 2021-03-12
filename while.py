# 백준 10952번 

import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if (A == 0 and B == 0):
        break
    print(A+B)

# 백준 10951번 

import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break 

# 백준 1110번 

N = int(input())
clear = N
N2 = 0
A = 0
count = 0
while True:
    A = N // 10 + N % 10
    N2 = (N % 10) * 10 + A % 10
    count += 1
    N = N2
    if N2 == clear:
        break
print(count)