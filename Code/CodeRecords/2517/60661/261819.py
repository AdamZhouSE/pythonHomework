res=0
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
n=len(a)
dic={}
for i in range(n):
    for j in range(n):
        if dic.get(a[i]+b[j])==None:
            dic[a[i]+b[j]]=1
        else:
            dic[a[i]+b[j]]+=1
for i in range(n):
    for j in range(n):
        if dic.get(-1*(c[i]+d[j]))!=None:
            res+=dic.get(-1*(c[i]+d[j]))
print(res)