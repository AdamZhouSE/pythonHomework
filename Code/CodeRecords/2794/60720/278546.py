n=int(input())
list0=input().split()
list0=[int(list0[i]) for i in range(n)]
k=int(input())
list1=input().split()
list1=[int(list1[i]) for i in range(k)]
for i in range(k):
    sum=0
    k1=list1[i]
    for j in range(n):
        sum+=list0[j]
        if k1<=sum:
            print(j+1)
            break
