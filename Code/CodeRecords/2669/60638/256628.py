n=int(input())
for x in range(0,n):
    num=int(input())
    i=num
    while i >=0:
        if i&num==i:
            print(i,end=" ")
        i=i-1
    print()