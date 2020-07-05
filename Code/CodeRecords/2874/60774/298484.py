n = int(input())
routine = list(map(int,input().split(' ')))
yesterday = routine[0]
rest = 0
for i in range(1,n):
    today = routine[i]
    if(today == 4):
        if(yesterday == 2):
            today == 3
        elif(yesterday == 3):
            today == 2
    if(today == 1):
        rest = rest + 1
    elif(today == yesterday and today != 4):
        rest = rest + 1
    yseterday = today
print(rest)