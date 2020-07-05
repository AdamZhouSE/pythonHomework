tests=(int)(input())
for i in range(0,tests):
    n=input().split(" ")
    sum=0
    for i in range(1,(int)(n[1])+1):
        sum+=i
    if(sum<=(int)(n[0])):
        print(1)
    else:
        print(0)