# 백준 1330번 

a, b = map(int, input().split())

if (a > b):
    print('>')
elif (a == b):
    print('==')
else:
    print('<')

# 백준 9498번

num = int(input())

if 90 <= num <= 100:
    print('A')
elif 80 <= num <= 89:
    print('B')
elif 70 <= num <= 79:
    print('C')
elif 60 <= num <= 69:
    print('D')
else:
    print('F')

# 백준 2753번

num = int(input())

if ((num%4)==0 and (num%100)!=0 or (num%400)==0):
    print('1')
else:
    print('0')

# 백준 14681번 

x = int(input())
y = int(input())

if (x >= 1 and y >= 1):
    print('1')
elif (x <= -1 and y >= 1):
    print('2')
elif (x <= -1 and y <= -1):
    print('3')
else:
    print('4')

# 백준 2884번

H, M = map(int, input().split())

if (M > 44):
    print(H, M-45)
elif (M < 45 and H > 0):
    print(H-1, M+15)
else:
    print(23, M+15)