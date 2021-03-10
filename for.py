# 백준 2739번

N = int(input())

for i in range(1 , 10):
    print(N, '*', i, "=", N*i)

# 백준 10950번 

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A+B)

# 백준 8393번

n =  int(input())

for i in range(1,n):
    if (1 >= n <= 10000):
        break
    n = n + i
print(n)

# 백준 15552번

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

# 백준 2741번

N = int(input())

for i in range(1, N+1):
    print(i)