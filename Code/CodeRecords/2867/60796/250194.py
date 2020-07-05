ls=[]
heng=0
lie=0
for i in range(5):
    ls.append(input().split(" "))
    ls[i]=[int(x) for x in ls[i]]
for i in range(5):
    m=0
    for j in range(5):
        if ls[i][j]==1:
            heng=i
            lie=j
            m=1
            break
    if m==1:
        break
print(abs(2-heng)+abs(2-lie))
