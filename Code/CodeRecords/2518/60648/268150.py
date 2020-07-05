l1=eval('['+input()+']')
l2=eval('['+input()+']')
for i in range(1,10000):
    l3=l2
    for j in l3:
        for k in range(1,i):
            l3.append(j+k)
            l3.append(j-k)
    count=0
    for j in l1:
        for k in l3:
            if j==k:
                count+=1
                break
    if count==len(l1):
        print(i)
        break