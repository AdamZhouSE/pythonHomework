size=int(input())
for i in range(size):
    l=int(input())
    list0=input().split()
    count=0
    for j in range(l):
        for k in range(j+1,l):
            if list0[j]==list0[k]:
                count+=1
    print(count)