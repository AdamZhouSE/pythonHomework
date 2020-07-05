n=int(input())
for i in range(n):
    temp=input()
    A=int(temp[0])
    B=int(temp[2])

    sum=0
    i=0
    while i<=B:
        sum=sum+i
        i=i+1
    if sum<=A:
        print(1)
    else:
        print(0)