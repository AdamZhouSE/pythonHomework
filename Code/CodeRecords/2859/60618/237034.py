n=int(input())
line=[[0]*n]*n
for i in range(n):
    line[i]=input().split(' ')

result=1
for i in range(0,n):
    if line[i]!=line[n-i-1]:
        result=0
    if i==(n-1)/2:
        if line[i].reverse()!=line[i]:
            result=0
                
if result==0:
    print("NO")
else:
    print("YES")
    
