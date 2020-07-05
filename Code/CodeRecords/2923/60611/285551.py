import sys
number=list(map(int,input().split(" ")))
l=[]
for i in range(number[-1]+1):
    l.append(list(map(int,input().split(" "))))
tag=[0 for i in range(number[0])]
for i in range(1,1+number[1]):
    for j in range(l[i][0]-1,l[i][1]):
        tag[j]+=1
assist=sorted(l[0])
tag=sorted(tag)
count=0
for i in range(number[0]):
    count+=tag[i]*assist[i]
print(count)