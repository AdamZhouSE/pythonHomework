T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    n=arr[0]
    k=arr[1]
    array=[int(n) for n in input().split(' ')]
    num=n-k
    sum=[]
    for j in range(0,num+1):
        all=array[j]
        m=1
        while m<k:
           all=all+array[j+m]
           m=m+1
        sum.append(all)
    max=sum[0]
    for j in range(1,len(sum)):
        if sum[j]>max:
            max=sum[j]
    print(max)