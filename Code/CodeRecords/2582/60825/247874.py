aaa=input()
l1=aaa.split(",")
l1= list(map(int, l1))
aaa=input()
l2=aaa.split(",")
l2= list(map(int, l2))

res=0

for i in range(len(l1)):
    for j in range(len(l2)):
        res=max(abs(l1[i]-l1[j])+abs(l2[i]-l2[j])+abs(i-j))
    
print(res)