n=int(input())
for x in range(0,n):
    list1=list(map(int,input().split(" ")))
    num=list1[0]
    k=list1[1]
    print((10-k)*(num-1))