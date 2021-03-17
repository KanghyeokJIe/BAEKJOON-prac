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

n = int(input())

for i in range(n):
    case = str(input())
    score = 0
    _count = 0
    for j in list(case):
        if j == "O":
            _count += 1
            score += _count
        elif j == "X":
            _count = 0

    print(score)

# 백준 4344번

c = int(input())

for i in range(c):
    result = list(map(int, input().split()))
    avg = sum(result[1:]) / result[0]
    count = 0
    for score in result[1:]:
        if score > avg:
            count += 1
    rate = count / result[0] * 100

    print(str('%.3f' % round(count / result[0] * 100, 3)) + '%')