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