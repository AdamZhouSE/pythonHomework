import math
def func5(m,n):
    arr=[0]*(n-m+1)
    op=0
    for i in range(len(arr)):
        arr[i]=util(m+i)
    output=arr[0]
    for i in range(1,len(arr)):
        for j in range(10):
            if output[j]!=arr[i][j]:
                output[j]=0
    for i in range(10):
        if output[i]=='1':
            op=op+math.pow(2,9-i)
    print(int(op))
def util(num):
    byte=[0]*10
    count=9
    while num>=1:
        if num%2==0:
            num=num/2
            count=count-1
        else:
            num=(num-1)/2
            byte[count]="1"
            count=count-1
    return byte

ip=eval(input())
func5(ip[0],ip[1])