a=int(input())
b=[int(i) for i in input().split()]
maxnum=0
for i in range(0,a):
    index=0
    for j in range(i+1,a):
        if b[i]==b[j]:
            index+=1
    if index>maxnum:
        maxnum=index
print(maxnum+1)