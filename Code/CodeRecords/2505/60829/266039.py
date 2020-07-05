bb=str(input()).split(",")
b=[]
for i in bb:
    b.append(int(i))
for i in range(0,len(b)):
    judge=0
    for j in range(1,len(b)):
        if b[i]==b[j] and not i==j:
            print(b[i])
            judge=1
            break
    if judge==1:
        break