s=input()
n=eval(s)
num=len(n)
dica={i:{i} for i in range(num)}
res=num
for i in range(num):
    for j in range(i,num):
        if n[i][j]==1 and dica[i] is not dica[j]:
            dica[i]=dica[i]|dica[j]
            for k in dica[j]:
                dica[k]=dica[i]
            res-=1
print(res)