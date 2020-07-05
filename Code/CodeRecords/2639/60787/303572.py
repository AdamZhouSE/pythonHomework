s=list(input())
k=int(input())
def count(i,j):
    l1=[]
    l2=[]
    for idx in range(i,j+1):
        if not s[idx] in l1:
            l1.append(s[idx])
            l2.append(1)
        else:
            l2[l1.index(s[idx])]+=1
    return max(l2)

re=0
temp=0
for i in range(0,len(s)-k):
    for j in range(i+k+1,len(s)):
        temp=count(i,j)+k
        if temp==j-i+1:
            if temp>re:
                re=temp
print(re)