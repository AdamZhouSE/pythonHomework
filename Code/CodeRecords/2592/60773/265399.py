num=int(input())
for k in range(num):
    r=int(input())
    sum=0
    for i in range(1,2*r,1):
        for j in range(1,2*r,1):
            if (i*i+j*j)**0.5<=2*r:
                sum=sum+1
    print(sum)