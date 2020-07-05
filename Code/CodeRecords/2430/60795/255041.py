T=int(input())
for i in range(0,T):
    num=int(input())
    arr=[int(n) for n in input().split(' ')]
    k=int(input())
    re=[]
    for j in range(0,num):
        a=arr[j]
        for z in range(j+1,num):
            b=arr[z]
            if a+b==k:
                re.append(a)
                re.append(b)
                break
    if len(re)==0:
        print(-1)
    else:
        z=0
        while z<len(re):
            print(re[z],end=" ")
            print(re[z+1],end=" ")
            print(k)
            z=z+2
            