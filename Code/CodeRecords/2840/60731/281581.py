n,k=map(int,input().split())
data=input().split()
res=0
for i in range(n):
    numof4=data[i].count('4')
    numof7=data[i].count('7')
    if numof4+numof7<=k:
        res+=1
print(res)