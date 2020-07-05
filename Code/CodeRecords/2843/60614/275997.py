length=int(input())
a=[int(x) for x in input().split()]
b=[0]*length
for i in range(length-1,-1,-1):
    b[i]=a[i]
    for j in range(i+1,length):
        if (j-i)%2==1:
            b[i]+=b[j]
        else:
            b[i]-=b[j]
print(" ".join([str(x) for x in b]))