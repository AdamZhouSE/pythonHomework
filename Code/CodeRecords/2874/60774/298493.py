n = int(input())
routine = list(map(int,input().split(' ')))
yesterday = routine[0]
for i in range(1,n):
    today = routine[i]
    if(today == 3):
        if(yesterday == 2):
            today = 1
        elif(yesterday == 1):
            today = 2        
    if(today == yesterday and today != 3):
        today = 0
    routine[i] = today
    yesterday = today
print(routine.count(0))