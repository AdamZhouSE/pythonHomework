n=int(input())
for x in range(0,n):
    num= int(input())//2
    ways=[0]*(num+1)
    for i in range(0,len(ways)):
        if i ==0:
            ways[i]=1
            continue
        if i == 1:
            ways[i]=1
            continue
        for j in range(0,i):
            ways[i]=ways[i]+ways[j]*ways[i-1-j]
    print(ways[num])