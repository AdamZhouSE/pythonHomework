num=int(input())
for n in range(num):
    size=int(input())
    lst=list(map(int,input().split(' ')))
    lst.sort()
    for i in range(1,size+1):
        if i!=lst[i-1]:
            print(i)
            break