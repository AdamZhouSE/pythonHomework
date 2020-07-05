n=int(input())
temp=[]
for x in range(1,n+1):
    temp.append(x)
res=""
for h in temp:
    res+=str(h)
print(res[n-1])