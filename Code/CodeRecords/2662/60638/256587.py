n=int(input())
for x in range(0,n):
    num=bin(int(input()))
    sum=0
    for i in range(2,len(num)):
        if num[i]=="1":
            sum=sum+1
    if sum%2==0:
        print("even")
    else:
        print("odd")