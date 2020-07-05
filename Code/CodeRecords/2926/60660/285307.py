import  collections
n=int(input())
l1=eval('['+input().replace(' ',',')+']')
l2=[]
c=collections.Counter(l1)
result=0
for i in c:
    result=max(c[i],result)
print(result)