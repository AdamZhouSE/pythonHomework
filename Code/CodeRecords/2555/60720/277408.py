n=int(input())
list0=input().split()
list0=[int(list0[i]) for i in range(len(list0))]
sum=0
for i in range(len(list0)):
    for j in range(i+1,len(list0)):
        for k in range(j+1,len(list0)):
            if list0[i]<list0[j]<list0[k]:
                sum+=1
print(sum,end='')