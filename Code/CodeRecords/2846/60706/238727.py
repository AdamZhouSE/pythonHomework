n=int(input())
list4=input().split()
for i in range(0,n):
    for j in range(i+1,n):
        if list4[i]==list4[j]:
            list4[j]='0'
ans=0
for i in range(0,n):
    if list4[i]=='0':
        continue
    else:
        ans=ans+1
print(ans)