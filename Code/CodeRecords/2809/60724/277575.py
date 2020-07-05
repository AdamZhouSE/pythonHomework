n=int(input())
num=input().split()
num=[int(i) for i in num]
chang=[]
kuan=num.copy()
res=[]
for i in range(n-1):
    chang.append(num[i])
    kuan.remove(num[i])
    changlen=sum(chang)
    kuanlen=sum(kuan)
    res.append(changlen*changlen+kuanlen*kuanlen)
print(max(res))