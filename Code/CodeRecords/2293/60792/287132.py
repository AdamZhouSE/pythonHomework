num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    k=int(input())
    list1.sort()
    print(list1[k-1])