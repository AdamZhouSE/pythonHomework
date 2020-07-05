n=int(input())
list0=[]
for k in range(n):
    list1=input().split(',')
    list1=[int(list1[i]) for i in range(n)]
    for i in range(n):
        list0.append(list1[i])
k=int(input())
list0.sort()
print(list0[k-1])