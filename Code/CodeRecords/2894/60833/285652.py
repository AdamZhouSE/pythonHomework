n=int(input())
str1=str(input())
res=0
judge=1
for i in range(0,n-1):
    if (str1[i:i+2]=='VK'):
        res+=1
    if((str1[i:i+2]=='VV')|(str1[i:i+2]=='KK')):
        if judge:
            res+=1
            judge=0
print(res,end='')