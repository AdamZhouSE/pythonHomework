n=int(input())
l1=input().split(" ")
l2=input().split(" ")
re=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if l2.index(l1[i])>l2.index(l1[j]):
            re+=1
print(re)