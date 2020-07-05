def Connellseq(n):
    i=0
    naturalodd=[value for value in range(1,n,2)]
    print(naturalodd)
    naturaleven=[value for value in range(2,n,2)]
    for j in range(1,n):
        if(i<n):
            i=i+j
            if(j%2==1):
                for odd in naturalodd[i:j]:
                    print(odd,end=" ")
            else:
                for even in naturaleven[i:j]:
                    print(even,end=" ")
        else:
            break

n=int(input(""))
for i in range(n):
    Connellseq(int(input("")))