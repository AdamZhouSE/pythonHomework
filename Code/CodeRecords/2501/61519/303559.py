n=int(input())
one=list(input().split(" "))
two=list(input().split(" "))
res=0
for i in range(n):
    n1=0
    n2=0
    left=one[i]
    for j in range(i+1,n):
        right=one[j]
        for k in range(n):
            if left==two[k]:
                n1=k
            if right==two[k]:
                n2=k
        if n2<n1:
            res+=1
print(res)