n=int(input())
str1=str(input())
res=0
for i in range(0,n-1):
    if (str1[i:i+2]=='VK'):
        res+=1
    elif(str1[i:i+2]=='KV'):
        res+=1
print(res,end='')