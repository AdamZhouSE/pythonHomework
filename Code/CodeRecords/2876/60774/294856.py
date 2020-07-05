n = int(input())
lightLst = list(map(int,input().split(' ')))
count = 0
for i in range(1,n - 1):
    if(lightLst[i - 1] == 1 and lightLst[i + 1] == 1 and lightLst[i] == 0):
        lightLst[i + 1] = 0
        count = count + 1
print(count)