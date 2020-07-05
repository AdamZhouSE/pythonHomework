t=input().split()
n=int(t[0])
k=int(t[1])
arr=input().split()
res=0
for i in range(0,n):
    if arr[i].count('4')+arr[i].count('7')<=k:
        res+=1
print(res)
