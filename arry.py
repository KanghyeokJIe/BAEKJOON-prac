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