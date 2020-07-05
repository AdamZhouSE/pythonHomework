t=int(input())
for i in range(t):
    num=int(input())
    n=[int(n) for n in input().split()]
    sum=0
    for j in range(0,num):
        sum+=n[j]
    if sum%3==0:
        print("1")
    else:
        print("0")
    