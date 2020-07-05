timeline, limit = input().split()
time = list(map(int, input().split()))

words = 1
for i in range(time.__len__()-1):
    if int(time[i+1]) - int(time[i]) > int(limit) and i == time.__len__()-2:
        words = 0
    elif int(time[i+1]) - int(time[i]) > int(limit) and i != time.__len__()-2:
        words = 1
    else:
        words = words+1
print(words)