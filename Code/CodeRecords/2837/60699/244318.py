list1=list(map(int,input().split(' ')))
n=list1[0]
l=list1[1]
r=list1[2]
index=1
list2=[]
for i in range(0,21):
    list2.append(index)
    index*=2
min=n-l
for i in range(0,l):
    min+=list2[i]
max=list2[r-1]*(n-r)
for i in range(0,r):
    max+=list2[i]
print(min,end=" ")
print(max)