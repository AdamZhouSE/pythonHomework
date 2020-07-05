a=int(input())
b=input().split(' ')
for i in range(0,len(b)):
    b[i]=int(b[i])
result="NO"
for i in range(0,len(b)-2):
    for j in range(i+1,len(b)-1):
        for k in range(j+1,len(b)):
            if max(b[i],b[j])-min(b[i],b[j])<b[k] and b[k]<b[i]+b[j]:
                result="YES"
                break
        if(result=="YES"):
            break
    if(result=="YES"):
        break
print(result)