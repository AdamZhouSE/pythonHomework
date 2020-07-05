num=int(input())
targets=[int(x) for x in input().split()]
max=num
for i in range(num):
    temp=[i]
    now=i
    while True:
        now=targets[now]-1
        if now in temp:
            if len(temp)<max:
                max=len(temp)
            break
        else:
            temp.append(now)
print(max)