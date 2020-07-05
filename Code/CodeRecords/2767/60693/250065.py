def find_ways(n):
    if n<10:
        if n==0 or n==3 or n==5 or n==6 or n==8 or n==9:return 1
        else:return 0
    res=0
    if n>10:
        tmp=n//10
        res+=tmp*2
        n=n%10
    if n==0 or n==3 or n==5 or n==6 or n==8 or n==9:return res
    else:return 0

cases=int(input())
for i in range(cases):
    n=int(input())
    print(find_ways(n))