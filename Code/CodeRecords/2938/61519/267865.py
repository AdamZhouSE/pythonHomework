list=[]
for i in range(1,10):
    list.append(i)
    for j in range(10):
        if (i==1) & (j==1):
            list.append(100)
        list.append(i*10+j)
for m in range(0,100):
    print(list[m])