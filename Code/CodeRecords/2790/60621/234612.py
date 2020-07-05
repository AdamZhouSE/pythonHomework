temp1=[int(x) for x in input().split()]
temp2=[int(x) for x in input().split()]
temp3=[int(x) for x in input().split()]

c=""
for i in range(temp1[1]):
    d=0
    for j in range(temp1[0]):
        if(temp2[j]<=temp3[i]):
            d+=1
    c=c+str(d)+" "
print(c.rstrip())