n = int(input())
days = [int(i) for i in input().split(" ")]
rest = 0
for i in  range(n-1):
    if(days[i]==0):
        rest+=1
    elif days[i] == 1:
        if days[i+1] == 1 :
            days[i+1] = 0
        elif days[i+1] == 3:
            days[i+1] = 2
    elif days[i] ==2:
        if days[i+1] == 2 :
            days[i+1] = 0
        elif days[i+1] == 3:
            days[i+1] = 1
if days[n-1] ==0:
    rest+=1
print(rest)