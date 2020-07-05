n=int(input())
f=list(map(int,input().split()))  
result="NO"
for i in range(n):
    if(f[f[f[i]-1]-1]-1==i):
        result="YES"
print(result)