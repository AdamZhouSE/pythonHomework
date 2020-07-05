n=int(input())
for i in range(0,n):
    input()
    list1=list(map(int,input().split(' ')))
    k=1
    while True:
        if k in list1:
            k+=1
        else:
            print(k)
            break