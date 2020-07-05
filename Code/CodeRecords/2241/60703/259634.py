n = int(input())
res = 0
for i in range(1,n+1):
    temp = 0#下面从i开始，包含了自己
    for j in range(i,n+1):
        temp+=j
        if(temp==n):
            res+=1
            break
        elif(temp>n):
            break
print(res)