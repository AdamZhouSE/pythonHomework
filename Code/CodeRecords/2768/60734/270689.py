def divide(a,b,m):
    count=0
    num = m
    while num<=b:
        if num>=a:
            count+=1
        num+=m
    return count

t = int(input())
for i in range(t):
    lst = list(map(int,input().split(' ')))
    print(divide(lst[0],lst[1],lst[2]))