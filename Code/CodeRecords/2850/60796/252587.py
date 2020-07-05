n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
result=[]
for i in range(n):
    for k in range(i,n):
        l=[]
        for a in range(0,n):
            l.append(ls[a])#注意：不能直接用l=ls，因为这样并不是把ls赋值给l，而是使得ls、l都指向了同一个数组ls
        #print("i",i," k:",k)
        for j in range(i,k+1):
            l[j]=1-l[j]
        #print(l)
        result.append(l.count(1))
print(max(result))
