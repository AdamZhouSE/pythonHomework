N=int(input())
result=1
for i in range(1,N//2+2):
    temp=0
    for j in range(i,N):
        temp+=j
        if(temp== N):
            result+=1
            break
        if(temp>N):
            break
print(result)