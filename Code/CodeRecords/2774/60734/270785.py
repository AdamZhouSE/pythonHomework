t = int(input())
for i in range(t):
    lst = list(map(int,input().split(' ')))
    n,k = lst[0],lst[1]
    lst = list(map(int,input().split(' ')))
    lst.sort()
    count = 0
    while k>0:
        k = k-lst[count]
        count+=1
    print(count-1)
    