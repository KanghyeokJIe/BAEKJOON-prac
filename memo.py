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