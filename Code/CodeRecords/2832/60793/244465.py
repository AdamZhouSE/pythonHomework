page_num = int(input())
a = list(map(int, input().split(" ")))
a = [i - 1 for i in a]
days = 0
pause = False
stop_point = a[0]
for i in range(0, page_num):
    stop_point = max(stop_point, a[i])
    if i == stop_point:
        days += 1
print(days)
