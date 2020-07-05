a=int(input())
b = input().split(' ')
for i in range(0, len(b)):
    b[i] = int(b[i])
result=0
countfu=0
kebian=0
for i in range(0,len(b)):
    if max(b[i],1)-min(b[i],1)<max(b[i],-1)-min(b[i],-1):
        result=result+max(b[i],1)-min(b[i],1)
    elif(max(b[i],1)-min(b[i],1)==max(b[i],-1)-min(b[i],-1)):
        result = result + max(b[i], 1) - min(b[i], 1)
        kebian=1
    else:
        result=result+max(b[i],-1)-min(b[i],-1)
        countfu=countfu+1
if(countfu%2==1 and kebian==0):
    result=result+2
print(result)