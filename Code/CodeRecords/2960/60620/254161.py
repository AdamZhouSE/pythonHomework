m,n=map(int,input().split())
a=input()
b=input()
num=0
result=[]
for i in range(n-m+1):
    if(b[i]!='*'):
        if(b[i]==a[0]):
            for j in range(1,m):
                if(a[j]!='*'and a[j]==b[i+j]):
                    if(j==m-1):
                        num+=1
                        result.append(i+1)
                    continue
                elif(a[j]=='*'):
                    if(j==m-1):
                        num+=1
                        result.append(i+1)
                    continue
                else:break                
    else:
        for j in range(1,m):
            if(a[j]!='*'and a[j]==b[i+j]):
                if(j==m-1):
                    num+=1
                    result.append(i+1)
                continue
            elif(a[j]=='*'):
                if(j==m-1):
                    num+=1
                    result.append(i+1)
                continue
            else:break
if(num==0):print(0,' ')            
else:
    print(num,)
    print(*result,'')  