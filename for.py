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

# 백준 11021번

import sys
T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i+1,A+B))

# 백준 11022번

import sys
T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i+1,A,B,A+B))

# 백준 2438번

N = int(input())

for i in range(1,N+1):
    print('*'* i) 

# 백준 2439번

N = int(input())

for i in range(1,N+1):
    print(" "*(N-i) + '*'* i)   #" "*(N-i) 을 통해 오른쪽으로 별을 밀어서 쓴다.

# 백준 10871번

import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")