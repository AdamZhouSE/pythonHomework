n=int(input())
line=[[0]*n]*n
for i in range(n):
    line[i]=input().split(' ')
    
str1=','.join(line[0])
result=1
for i in range(0,n):
    
    str=','.join(line[i])
    for j in range(0,n):
        if i==j or i==n-j-1:
            if str[i]!=str1[0] or str[j]!=str1[0]:
                result=0
        else:
            if str[i]!=str1[1] or str[j]!=str1[1]:
                result=0
        if str[j]!=str[n-j-1]:
            result=0

if result==0:
    print("NO")
else:
    print("YES")
    
