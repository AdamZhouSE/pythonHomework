n = int(input())
routine = list(map(int,input().split(' ')))
yesterday = routine[0]
rest = 0
for i in range(1,n):
    today = routine[i]
    if(today == 3):
        if(yesterday == 2):
            today = 1
        elif(yesterday == 1):
            today = 2
    if(today == 0):
        rest = rest + 1
    elif(today == yesterday and today != 3):
        rest = rest + 1
    yesterday = today
print(rest)