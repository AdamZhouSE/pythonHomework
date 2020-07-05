n=int(input())
list1=[]
for j in range(n):
    list1.append(int(input()))
ans=0
for i in range(1,n+1):
    j=i
    k=1
    while list1[j-1]!=-1:
        k+=1
        j=list1[j-1]
    if ans<k:
        ans=k
print(ans)