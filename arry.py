# 백준 10818번 

N = int(input())
A = list(map(int, input().split()))

print('{} {}'.format(min(A),max(A)))

# 백준 2562번

A = []

for i in range(9):
    A.append(int(input()))

print(max(A))
print(A.index(max(A))+1)

# 백준 2577번 

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))

# 백준 3052번

a = []

for i in range(10):
    n = int(input())
    a.append(n % 42)

a = set(a)
print(len(a))

# 백준 1546번

a = int(input())
b = list(map(int, input().split()))
b_max = max(b)

for i in range(a):
    b[i] = b[i] / b_max * 100

avg = sum(b) / a
print('{}'.format(avg))

# 백준 8958번

