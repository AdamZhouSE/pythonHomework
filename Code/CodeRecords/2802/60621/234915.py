a=[int(x) for  x in input().split()]
b=[int(x) for  x in input().split()]
people=a[0]
m=a[1]
while(people>0):
    for i in range(len(b)):
        if(b[i]>0):
            b[i]-=m
            if(b[i]<=0):
                people-=1
                if(people==0):
                    print(i+1)