n=int(input())
for i in range(0,n):
    k=int(input())
    first=(2+(k-1)*2)*(k-1)/2+1
    count=k*2
    last=first+count-1
    sum=int((first+last)*count/2)
    print(sum)