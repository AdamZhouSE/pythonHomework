n=int(input())
Target=list(map(int,input().split()))
data=[]
for i in range(n):
    data.append([i+1])
round=1
while(True):
    round+=1
    is_end=False
    for i in range(n):
        if(Target[i] in data[i]):
            is_end=True
            break
        else:
            data[Target[i]-1]+=data[i]
    if(is_end):
        break;
print(round)