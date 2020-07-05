n=int(input())
floor=[int(i) for i in input().split()]
m=int(input())
books=[int(i) for i in input().split()]
for book in books:
    sum=0
    for i in range(0,n):
        sum+=floor[i]
        if sum>=book:
            re=i+1
            break
    print(i+1)