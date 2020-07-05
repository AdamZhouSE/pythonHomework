n=int(input())
for i in range(0,n):
    num=int(input())
    x=[int(x) for x in input().split(" ")]
    max=0
    y=x[0]
    for j in range(1,len(x)):
        if  x[j]>y:
            max=j
            y=x[j]
    left=0
    right=0
    sum=0
    for k in range(0,max+1):
        if x[k]>left:
            left=x[k]
        else:
            sum=sum+left-x[k]
    for k in range(len(x)-1,max,-1):
        if x[k]>right:
            right=x[k]
        else:
            sum=sum+right-x[k]
    print(sum)